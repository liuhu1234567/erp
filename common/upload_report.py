import requests
# from common.do_config import api_host
# from common.get_token import token_scf_platform
from config.all_path import report_dir
import os
from common.do_mysql import MyMysql
import time
import uuid
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA


def encrypt(public_key, pwd):
    """RSA加密"""
    key = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    encrypt_text = cipher.encrypt(pwd.encode())
    r = base64.b64encode(encrypt_text).decode()
    return r


def api_common_loginConfig(api_host, x_appid_header):
    """获取rsaPubKey"""
    url = f'{api_host}/api-node/common/loginConfig'
    headers = {
        "x-appid-header": x_appid_header
    }
    r = requests.post(url, headers=headers)
    return r


def api_login(api_host, username, password, code):
    """密码登录"""
    url = f'{api_host}/api-uaa/login/password'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    rsaPubKey = api_common_loginConfig(api_host, '1').json()['datas']['rsaPubKey']
    payload = {
        "username": username,
        "password": encrypt(rsaPubKey, password),
        "code": code,
        "remember": True,
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "type": 1,
        "key": str(uuid.uuid4())
    }
    r = requests.post(url, headers=headers, json=payload)
    return r


def get_file_url(reprot_name):
    """获取文件url"""
    api_host = "https://uat-gateway.dianliantech.com"
    username = "aaaz000001"
    password = 'ab12345678'
    code = 'shuodz4sojc30zntgyce'
    r = api_login(api_host, username, password, code)
    r_data = r.json()['datas']
    token = f"{r_data['token_type']} {r_data['access_token']}"

    url = f'{api_host}/api-node/common/fileUpload'
    headers = {
        "x-appid-header": "2",
        "Authorization": token
    }
    report_path = os.path.join(report_dir, reprot_name)
    with open(report_path, 'rb') as f:
        file_b = f.read()
    files = {
        'uploadFile': (reprot_name, file_b)
    }
    try:
        r = requests.post(url, headers=headers, files=files)
        fileId = r.json().get('datas').get('fileId')
    except Exception as e:
        fileId = None
        print(f'上传报告发生错误：{e}')
    file_url = f"http://172.30.206.52:8100/{fileId}"
    return file_url










# def get_file_url(report_name):
#     """获取文件url"""
#     url = f'http://app.scf-uat.dianliantech.com/api-node/common/fileUpload'
#     headers = {
#         "x-appid-header": "1",
#         "Authorization": token_scf_platform
#     }
#     path = os.path.join(report_dir, report_name)
#     with open(path, 'rb') as f:
#         file_b = f.read()
#     files = {
#         'uploadFile': (report_name, file_b)
#     }
#     r = requests.request("POST", url, headers=headers, files=files)
#     fileId = r.json()['datas']['fileId']
#     file_url = f"http://172.30.206.52:8100/{fileId}"
#     return file_url



def insert_report(project, report_name, file_url):
    """上传报告到 metersphere"""
    projectid = {
        "电镀": "686f8fc7-8251-4650-8639-8a5da48ec154",
        "SCCP": "9f35bf7f-36ed-4fb6-8a73-f4d9fc6f70f1",
        "金点信": "73d44836-375a-4ffd-a817-b2e6a16bdace",
        "cloud": "d6ba9f42-6107-45a6-b209-c09f407939cb",
        "default": "f5c844d9-a4fa-11ec-a815-0242ac1e0a04"
    }
    project_id = projectid.get(project)
    report_code = str(time.time()).replace('.', '')
    db = MyMysql(
        host='172.30.206.57',
        user='root',
        password='Password123@mysql',
        port=3307,
        database='metersphere'
    )
    sql = F'''insert into metersphere.api_scenario_report(
            id,project_id,name,url_html,create_time,update_time,status,user_id,trigger_mode,execute_type,create_user,actuator,end_time,report_version,version_id,report_type)
            values (
            {report_code},"{project_id}","{report_name}","{file_url}",
            unix_timestamp(current_timestamp(3))*1000,unix_timestamp(current_timestamp(3))*1000,
            "Error","Crew","MANUAL","Saved","Crew","LOCAL",unix_timestamp(current_timestamp(3))*1000,2,
            "f2678995-0cf5-49b8-a23f-6380cf9d9c64","SCENARIO_INDEPENDENT")
        '''
    r = db.insert(sql)
    print(f'报告插入结果：{r}')
    db.close()

