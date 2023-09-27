from case_api.login_password import api_login_login, api_login_calculate, api_login_sendSms
from common.do_config import skyworth_partnership, skyworth_erp, host_partnership, host_erp
import requests
import json


def get_operator_token():
    """合伙运营商管理后台token"""
    payload = {}
    r = api_login_calculate(host_partnership, skyworth_partnership["platform"], payload)
    r_json = r.json()
    payload = {
        "type": 1,
        "phone": skyworth_partnership["username"],
        "verifyCodeObj": {
            "key": r_json["data"]["imgKey"],
            "verifyCode": r_json["data"]["imgValue"]
        }
    }
    r = api_login_sendSms(host_partnership, skyworth_partnership["platform"], payload)
    r_json = r.json()
    payload = {
        "username": skyworth_partnership["username"],
        "password": skyworth_partnership["password"],
        "code": r_json["data"],
        "type": 1
    }
    r = api_login_login(host_partnership, skyworth_partnership["platform"], payload)
    r_json = r.json()
    token = r_json["data"]["accessToken"]
    return token


def get_erp_token():
    """Noneerp系统token"""
    payload = {}
    r = api_login_calculate(host_erp, skyworth_erp["platform"], payload)
    r_json = r.json()
    payload = {
        "type": 1,
        "phone": skyworth_erp["username"],
        "verifyCodeObj": {
            "key": r_json["data"]["imgKey"],
            "verifyCode": r_json["data"]["imgValue"]
        }
    }
    r = api_login_sendSms(host_erp, skyworth_erp["platform"], payload)
    r_json = r.json()
    payload = {
        "username": skyworth_erp["username"],
        "password": skyworth_erp["password"],
        "code": r_json["data"],
        "type": 1
    }
    r = api_login_login(host_erp, skyworth_erp["platform"], payload)
    r_json = r.json()
    token = r_json["data"]["accessToken"]
    return token


def get_clean_token():
    """清洁能源登录-获取验证码"""
    url = "http://spv2-gateway.skyworthpv.cn/public/verifyCode/calculate"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': "ICPVOWNER",
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    payload = {}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    aa = r.json()['data']['imgKey']
    bb = r.json()['data']['imgValue']

    url = "http://spv2-gateway.skyworthpv.cn/public/sendSms"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': "ICPVOWNER",
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    payload = {"verifyCodeObj": {"key": aa, "verifyCode": bb}, "phone": "18617072385", "type": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    cc = r.json()['data']

    url = "http://spv2-gateway.skyworthpv.cn/login"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': "ICPVOWNER",
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    payload = {"username": "18617072385", "code": cc, "type": 2}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


token_erp = get_erp_token()
token_operator = get_operator_token()
# get_clean_token()
