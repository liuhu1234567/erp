import unittest
import requests
import json
from common.global_variable import customize_dict
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA
from common.do_config import skyworth_partnership, host_partnership, host_erp


# def encrypt(password):
#     """AES加密"""
#     # key为16的倍数
#     key = "6578904783439suw"
#     # 加密字符串长同样需要16倍数
#     aes = AES.new(key.encode(), AES.MODE_ECB)
#     padding_text = pad(password.encode(), AES.block_size, style='pkcs7')
#     encrypted_text = aes.encrypt(padding_text)
#     r = base64.b64encode(encrypted_text).decode()
#     return r


# def encrypt(pwd):
#     """RSA加密"""
#     public_key = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKSItqTh99pxpM9iRuqtFy/f81g3hTXCdGMPjWGgMTziNMxK60BmzOqw24bjXQQ+pgKQhSsPhxT4QsgaG0QbDE8CAwEAAQ=="
#     key = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
#     # print('key---------------------')
#     # print(key)
#     rsakey = RSA.importKey(key)
#     cipher = Cipher_pksc1_v1_5.new(rsakey)
#     encrypt_text = cipher.encrypt(pwd.encode())
#     r = base64.b64encode(encrypt_text).decode()
#     return r

def api_login_calculate(host, platform, payload):
    """获取图形码"""
    url = f"{host}/cwgf/public/verifyCode/calculate"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': platform,
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r


def api_login_sendSms(host, platform, payload):
    """获取验证码"""
    url = f"{host}/cwgf/public/sendSms"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': platform,
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r


def api_login_login(host, platform, payload):
    """登录"""
    url = f"{host}/cwgf/login"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': platform,
        'Content-Type': 'application/json',
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r



# def api_erp_login(platform,payload):
#     """erp后台登录"""
#     url = f"{host_erp}/login"
#     headers = {
#         'Proxy-Connection': 'keep-alive',
#         'platform': platform,
#         'Content-Type': 'application/json',
#     }
#     r = requests.post(url, data=json.dumps(payload), headers=headers)
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
# class LoginPassword(unittest.TestCase):
#     def test_login_password(self):
#         """账号正确，密码正确"""
#         payload = {}
#         r = api_login_calculate(host_partnership, skyworth_partnership["platform"], payload)
#         r_json = r.json()
#
#         payload = {
#             "type": 1,
#             "phone": "13823354268",
#             "verifyCodeObj": {
#                 "key": r_json["data"]["imgKey"],
#                 "verifyCode": r_json["data"]["imgValue"]
#             }
#         }
#         r = api_login_sendSms(host_partnership, skyworth_partnership["platform"], payload)
#         r_json = r.json()
#         payload = {
#             "username": skyworth_partnership["username"],
#             "password": skyworth_partnership["password"],
#             "code": r_json["data"],
#             "type": 1
#         }
#         r = api_login_login(host_partnership, skyworth_partnership["platform"], payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual("SYS000000", r_json['code'])
#
#
# if __name__ == '__main__':
#     aa = LoginPassword()
#     aa.test_login_password()
#     unittest.main()
