import requests
import unittest
import json
from common.global_variable import customize_dict
from common.do_config import host_partnership
from common.do_faker import get_number, get_phone, get_name
# from case_api.sign import chuangjian,p1_tijiao,fengxian,chukan,chusheshenhe,yunyingshnagbaojia,lixiangshenpi,suodanliebioa,xiangkan,chushefuhe,yunyingshanghejia,p2zhiliao,qianyezhiliao,jiafangshenhe,qianyue

data_order = {}
data_order['faker'] = get_number(8)
data_order['phone'] = get_phone()
data_order['name'] = get_name()
data_url = "http://spv3-gateway.skyworthpv.cn"
oldOrderNo = 'DH1153292464314351617'

def logen():
    url = f"{data_url}/public/verifyCode/calculate"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': "CONSTRUCTMANAGER",
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    payload = {}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['imgKey'] = r.json()['data']['imgKey']
    data_order['imgValue'] = r.json()['data']['imgValue']

    url = f"{data_url}/public/sendSms"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': "CONSTRUCTMANAGER",
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    payload = {"type": 1, "phone": "17585245519",
               "verifyCodeObj": {"key": data_order['imgKey'], "verifyCode": data_order['imgValue']}}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['sendSms'] = r.json()['data']

    url = f"{data_url}/login"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': "CONSTRUCTMANAGER",
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    payload = {
        "username": "17585245519",
        "password": "Hc2HktKFDRxv2gpIzcURTbZZJpYNbORfZi5cWizKgpN9HgT1r243/AXnfZxcrslKVmBYrWaHMWbZq+5JIc3J6+LoMMi4rioiK0rqsNNSd5B6yFClU0cPFmTJ3OSA5Y1E2rsht7FxcLsRT+y+oozVPTCLNnwnNN3ksbcFEdYVCEU=",
        "code": data_order['sendSms'],
        "type": 1
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['accessToken'] = r.json()['data']['accessToken']


# def objert():
#     url = 'http://spv3-gateway.skyworthpv.cn/api/token'
#     headers = {
#         'platform': 'CONSTRUCTMANAGER',
#         'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
#         'Content-Type': 'application/json',
#         'Accept': '*/*',
#         'Host': 'spv1-gateway.skyworthpv.cn',
#         'Connection': 'keep-alive',
#         'Cookie': 'HWWAFSESID=a4e4179c46c2f8a84c; HWWAFSESTIME=1694504585906'
#     }
#     payload = {
#         "clientId": "CONSTRUCT",
#         "clientSecret": "123456",
#         "scope": "CONSTRUCT"
#     }
#     r = requests.post(url, data=json.dumps(payload), headers=headers)
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     data_order['data_accessToken'] = r.json()['data']['accessToken']
# 
#     url = f'{data_url}/api/projectOrder/sync'
#     headers = {
#         'accessToken': data_order['data_accessToken'],
#         'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
#         'Content-Type': 'application/json',
#         'Accept': '*/*',
#         'Host': 'spv1-gateway.skyworthpv.cn',
#         'Connection': 'keep-alive',
#     }
#     payload = {
#         "oldOrderId": f"16500001993{data_order['faker']}",
#         "oldOrderNo": oldOrderNo,
#         "name": f"测试订单-{data_order['faker']}-流程测试",
#         "buildMode": "2",
#         "province": "330000",
#         "city": "330600",
#         "district": "330604",
#         "address": "香港大道910",
#         "businessDeptId": 122,
#         "developManagerId": 451,
#         "developManagerPhone": "17585245519",
#         "projectOwner": 1,
#         "epcContract1": "http://minio-test.skyworthpv.cn/user/test2/2023/9/5/1136662679625490432/16938805281680MTg3F.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230905T072447Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=96454ce16101e699f14223c1cbffe9867a8000d4989975900b1bfc54f8c79572",
#         "epcContract": "https://skyworthe-prod.oss-cn-hangzhou.aliyuncs.com/prod/HHR20230424026/1682336557170_2e181eb7.pdf",
#         "createTime": "2023-08-22 11:11:11",
#         "createUser": 451,
#         "createUserPhone": "17585245519"
#     }
#     r = requests.post(url, data=json.dumps(payload), headers=headers)
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')


def constructmanager():
    '''项目启动'''
    url = f"{data_url}/constructmanager/projectStartManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]
    data_order['orderId'] = r.json()['data']['data'][0]["orderId"]

    url = f"{data_url}/constructmanager/projectStartManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "constructMode": 2,
        "drawType": 1,
        "buildPic": [
            "http://minio-test.skyworthpv.cn/order/test1/2023/9/13/1151450055788302336/1694568725356oSB1Py.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230913%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230913T013205Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8e96ff35a2709820f14c5f23d6d4bf38b817da40be73fede2bcf544d71be8b5d"
        ],
        "structurePic": [
            "http://minio-test.skyworthpv.cn/order/test1/2023/9/13/1151450055788302336/1694568728134ApJgWQ.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230913%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230913T013208Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=7d3fa02c2724932f0cb7b4bcca00ef27d45a42b3cb4e07da71ceb15ec88ae7b8"
        ],
        "electricalPic": [
            "http://minio-test.skyworthpv.cn/order/test1/2023/9/13/1151450055788302336/1694568730820yBuGOu.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230913%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230913T013210Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6774ceee3caf27a5bac88c75187c2c27c4abf8deda7739a18c62f14b0fe611fe"
        ],
        "projectConfirmForm": "http://minio-test.skyworthpv.cn/order/test1/2023/9/13/1151450055788302336/16945687215447PYMCM.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230913%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230913T013201Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=3fa8930f76c9c9ed6a074a2be432268f5dcc46caa916b4e35cab3f1ab434b7cb",
        "othersUri": []
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def projectStartApprovalManager():
    '''项目启动审核'''
    url = f"{data_url}/constructmanager/projectStartApprovalManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/projectStartApprovalManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "status": 2,
        "projectDeptId": "133",
        "designerDeptId": "133",
        "projectManagerId": "450",
        "designerManagerId": "456",
        "remark": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def projectStartSpecificationManager():
    '''规格书上传'''
    url = f"{data_url}/constructmanager/projectStartSpecificationManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/projectStartSpecificationManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "inverterSpecification": [
            "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694663182480JAyC1x.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T034622Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=292c7ef470664374bf3526a65b224dca39838dd7821cd44876936b1c02d2cbae"
        ],
        "componentSpecification": [
            "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694663180806Zi0UUF.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T034620Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=73aa359eac37804a2d4f43bfbfe48e9d27b0f9b3b8b179cafc140f283df1d36d"
        ]
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def filingsDesignHandleManager():
    '''备案与接入办理'''
    url = f"{data_url}/constructmanager/filingsDesignHandleManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]
    url = f"{data_url}/constructmanager/filingsDesignHandleManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "certificateData": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/16946634766031vd2iW.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T035116Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=643381289e44070468177b9cd489c7015ef1d12651628949af42fbb6fba0c74b",
        "accessPlan": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694663478161tiBvWq.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T035118Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=763db7fca09da4b8239a08ed77071db588f7bea6b347f0710f026dd5b55be9d2",
        "powerGridReviewComments": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694663480959Y4wPnX.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T035120Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=1f204b5a66eca52c8d162c2d0ff437964bc7f54e48abe7527b42e5322af1553e",
        "accessApproval": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694663483467q7pxRH.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T035123Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=2048684c5ad5cd2c5cad2875ce7aa555b944ad789bea246b3614b22d4852bca4"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def filingsDesignStageManager():
    '''设计阶段'''
    url = f"{data_url}/constructmanager/filingsDesignStageManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/filingsDesignStageManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "needReinforcement": 1,
        "projectDetailForm": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694663691640i7hJcW.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T035451Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=0d53dd2b1182d64fb7837297b3e3b84bf8d7169912ce535751682eb74b48a7d9",
        "constructDrawing": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694663690036KehVBk.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T035450Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=1b9a1996dfdff5412b8057d7b3392d4801fdc314bfcec41383f776d9f43d8c1d",
        "loadReport": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694663696462g9xWDv.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T035456Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=cda7bf5a14d13bc6e0a5a6d2aa7ffc251370a5c9f127b5a51ce82b00b0695ad9",
        "reinforcementPlan": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694663694455ACmoz3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T035454Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=fb873c296a49fcc06b0e6334ea4a285e120a4a7346592d391b2546c62f7972db"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def filingsDesignApprovalManager():
    '''设计审核'''
    url = f"{data_url}/constructmanager/filingsDesignApprovalManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/filingsDesignApprovalManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"id": data_order['id'], "orderId": data_order['orderId'], "status": 2, "remark": None}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def filingsArrivalPlanManager():
    '''到货计划'''
    url = f"{data_url}/constructmanager/filingsArrivalPlanManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/filingsArrivalPlanManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "deviceArrivalPlanForm": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670252292XkZv1K.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054412Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=0741380bdbc7011c1e8b0df3a7aac8106a7c02c3f4b7af5955135339fc8817dc"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def filingsDrawingApprovalManager():
    '''图纸评审'''
    url = f"{data_url}/constructmanager/filingsDrawingApprovalManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/filingsDrawingApprovalManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"id": data_order['id'], "orderId": data_order['orderId'], "status": 2, "remark": None}

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def constructApplyManager():
    '''开工申请'''
    url = f"{data_url}/constructmanager/constructApplyManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/constructApplyManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "levelThreeSchedule": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670463940NbmR9a.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054743Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=4f9e26943f0c2136e1f8aaf5a6b2b323dcfb67c27a1288e8232dfae30cda6438",
        "projectTargetDuty": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/16946704655462KdGpR.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054745Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b1ba295f8124342a4204854f2dc4669644993c62d336a4098ccd6fc756359c53",
        "ownerDisclosureRecord": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670467486ouH9Se.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054747Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=54bf7e7c630b78e4af6379d6623b6ac6584ad6ceed817ae4bba08a17dba39a14",
        "startReport": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670469176NUS5V4.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054749Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9c8852fa4d623faebdb532dad735bc6bec3d3d9bd42d01027a1667a5bfef7410",
        "techDisclosure": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/16946704714079qbvR2.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054751Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8959970a8fa85312dee17e5a6443bccaf6198db022642ee491b7f68c93b32013",
        "qaTechDisclosure": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670473264qX00TF.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054753Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=1bfb5cfad037e90e5f97e44919979f31560d096d14a8bd3b9f7897ac10303419",
        "orgDesign": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670475374dX5nzw.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054755Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=022f39b5fef5b774290faa8bb25d39e6128e58a7cb1dbcb8838048725022e441",
        "hseMgtPlan": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670477842gDdkPg.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054757Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6101de3c034efbe644a3bfb4cacbb7f14cbe2a888f546a2f255b89be35d883b3",
        "projectSubcontract": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670481665j1TWhE.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T054801Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=35ecfa4b5e423458ed1ccdaa45d20a5a3057256d12be276422851c3d267b0007"
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def constructApplyApprovalManager():
    '''开工申请审核'''
    url = f"{data_url}/constructmanager/constructApplyApprovalManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/constructApplyApprovalManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"id": data_order['id'], "orderId": data_order['orderId'], "status": 2, "remark": None}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def constructStartInsureManager():
    '''保险购买'''
    url = f"{data_url}/constructmanager/constructStartInsureManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/constructStartInsureManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "allRiskInsure": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670699867UKFtIp.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T055139Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=44ecf13c243a579443597508fbe74175718feee5e9f7a0b2f48a03e43989997e",
        "accident": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/169467070181575K04v.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T055141Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8121bcb0bc349289fa272a31d53b486d9dbde89bccdc8feb13d04e13d8e8dcea"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def constructStartManager():
    '''开工起动'''
    url = f"{data_url}/constructmanager/constructStartManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/constructStartManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "haveSteelTiles": 1,
        "pulloutTestImages": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151811891360436224/1694670838139oV1fAW.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T055358Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=4a0c4fe21228af47cd1cc93a6ffc6d66d3376ef9670aaf15a796f53d1bb2140f"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def constructStartApprovalManager():
    '''开工起动审核'''
    url = f"{data_url}/constructmanager/constructStartApprovalManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/constructStartApprovalManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"id": data_order['id'], "orderId": data_order['orderId'], "status": 2, "remark": None}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def constructStartConfirmManager():
    '''开工确认'''
    url = f"{data_url}/constructmanager/constructStartConfirmManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "constructStartPic": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694677530477ZfVf8R.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T074530Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=1b850eb4bda01b07b46b5073c507e83493f658b7512f783dc6145b364e840ed2",
        "orderId": data_order['orderId']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def reinforceAcceptanceManager():
    '''加固验收'''
    url = f"{data_url}/constructmanager/reinforceAcceptanceManager/upload"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "reinforceAcceptanceReport": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694677664902Q4NQw1.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T074744Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6dbea09b04c1c416e71aa5b6173bd9b074b54bda5d96f5b166bf1c3110d98fb8",
        "orderId": data_order['orderId']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def reinforceFirstApprovalManager():
    '''加固验收初审'''
    url = f"{data_url}/constructmanager/reinforceFirstApprovalManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"status": "2", "remark": None, "orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def reinforceReviewApprovalManager():
    '''加固验收复审'''
    url = f"{data_url}/constructmanager/reinforceReviewApprovalManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"status": "2", "remark": None, "orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def constructCollectInfoManager():
    '''施工阶段收资'''
    url = f"{data_url}/constructmanager/constructCollectInfoManager/page"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"oldOrderNo": oldOrderNo, "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['data'][0]["id"]

    url = f"{data_url}/constructmanager/constructCollectInfoManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "materialManagementSubmitReqWebDTO": {
            "id": data_order['id'],
            "orderId": data_order['orderId'],
            "materialIn": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678010002ynTpTE.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075330Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b7015af9286c16e569676635bebf494b5cd944b9d6a5295266ba8af394101004",
            "equipmentUnpackApproval": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678012495zgQ25x.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075332Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=85c720eef8113dc9cc394188754ae4a55098a4b179958bb1d7eb59c954a7994b",
            "materialSupplement": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678016819vitoT6.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075336Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=df35c1fe8fdc30b430a05b33799f354a2cf9b33d4b15e1d7f5d4299e5a5df668"
            ],
            "materialSupplementApproval": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678018249UjXMm4.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075338Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9595e5102bd3666bbd01f5917596d63be5e068c8a397f3e7e8ed0117ddfb4e97"
            ],
            "materialReturn": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678019878gyhZ5t.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075339Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=62b1cf043edb9b46ec74a8c8c51105a8b9fccbfe9b954a0dbd45aea4efff1792"
            ],
            "materialReturnApproval": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678021682JLcJOY.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075341Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=a4b3be4f3afa3d55826a09c55e5fe82655c3aa9d81290db8d5aaf78de0c16af9"
            ]
        },
        "constructionManagementSubmitReqWebDTO": {
            "qualityAcceptanceAndEvaluationTable": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678029586pLCNGS.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075349Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f3e99106c3d46f2ce8c3244748f5360990cf11b97f2b9da13ea64672e69d5289",
            "subitemQualityAcceptanceRecord": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/16946780328144lhsHG.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075352Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=467cdbddfcd927a49381976e02482fce18c639d7146a432b8370d6220073bff7",
            "inspectRecord": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678035174CTewtq.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075355Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=06fdea0431b87dadcf019baf019cb4440f43b0957f17e403a08fc483d78980ca"
            ],
            "workContactRecord": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678037987SJBDJl.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075358Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=5231ab00107c0ef1f7d4122c67846733b84ec77d9bbe568a64238a1766fd7fa3",
            "orderId": data_order['orderId'],
            "id": data_order['id']
        },
        "testInspectionSubmitReqWebDTO": {
            "bracketInspectionPhoto": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678044563Hw6Vyu.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075404Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=4d1af08e02e7bf2efd9cdf6f4da3e55eb152590d1201efca48fd074b8cc20db9",
            "bracketInspectionReport": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678046173FDaOgY.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075406Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=ceee7576cd488cfa6c1fe1eb029000bc4bdfbb9bd19ab65895736807ffd20928",
            "cementFoundationTestPhoto": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/16946780485737atuHq.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075408Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6e63fe8dbc9ce0119787307d45c9dd4f70f47608bbeff9e806263d6bb7448b52",
            "cementFoundationTestReport": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678050696xZGhKb.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075410Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6dc9383c59362a8b45ed96adbd8634cfc2e421a56af7b210939f45cac8a355a1",
            "cementRectificationNotice": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678052840IjgsBX.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075412Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=2057c06669ea37a5c032f642bc005b82e09fefb80a7a62230675ec9dc6df3375",
            "cementRectificationPhoto": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678054866Ed4Gf2.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075414Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=93a890b1680585326e51b68b402441d00ec30ccc34de71bab4cb2dabd3af7852",
            "voltageType": 0,
            "primarySecondaryEquipmentThirdPartyInspectionReport": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678058921CSpmgq.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075418Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=0afeb6cd6c1ffa1383edde4c0020c47107eb9bbcad06cff403714aaf5db3dec4",
            "parallelCabinetThirdPartyInspectionReport": None,
            "cableThirdPartyInspectionReport": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678060526c87LWN.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075420Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d2fb043bf50203e2d89dba64cdc41e67bfa8db83ac8b6bf455a7f8fdebef43b4"
            ],
            "orderId": data_order['orderId'],
            "id": data_order['id']
        },
        "safeManagementSubmitReqWebDTO": {
            "constructionPersonnelQualificationFile": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678065432sm6wEH.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075425Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=01c7e2b3c26bdb427f5257e2cd36b0e0755c97c57fde87ec688e462e05309dc9",
            "constructionFacilityConfigurationDeclarationForm": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678067321viFHRr.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075427Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=26f8d6d74ddc33bc2ac3cdb0b6afd9c4b6c70b0f928d4149c25b6a8c0e6cf8da",
            "constructionLargeMediumMachineMove": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/16946780697301DJpem.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075429Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=3aea34e208f05cb0d3ae7d11bb0a93d6735aefb0068d1cf712d4294ded3ea324",
            "orderId": data_order['orderId'],
            "id": data_order['id']
        },
        "drawingManagementSubmitWebReqDTO": {
            "designChangeOrder": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678072454A8etyz.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075432Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=a3e64706eea8dd0e00f9f3efb010819538fa354f38c2ede7deb342f5b8a298cf"
            ],
            "revisedConstructionDrawing": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/16946780761075ELrhQ.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075436Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=04415c1b4a6b3453b49526be38d511a252fda110ea5bc5feb6bf91eb0b8cc65f"
            ],
            "constructOthers": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678078443lGqjz8.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075438Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d5b5bfb16734dfca67554f659bd00bf2ea6e53ab4871f57e6e82eb1a6446764f"
            ],
            "orderId": data_order['orderId'],
            "id": data_order['id']
        },
        "projectVisaSubmitReqWebDTO": {
            "constructVisaApply": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678083039zFUZYH.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075443Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d17f92574820edf62b6b21404a92f81dbd632d7e9357a33cacd95c279d44cb3d"
            ],
            "constructVisaConfirm": [
                "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151906362907475968/1694678085113nBQ2tU.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T075445Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6e1f20f37d5467ec5db6d29c694fcd077755f091fb85748703913ed5bdff8729"
            ],
            "orderId": data_order['orderId'],
            "id": data_order['id']
        },
        "id": data_order['id'],
        "orderId": data_order['orderId']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def acceptConnectedManager():
    '''并发电网'''
    url = f"{data_url}/constructmanager/acceptConnectedManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "connectedMeterReading": [
            "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694684823523vidhAW.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T094703Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9faffa0410e8464850ab1fd7f4d512fec38011aba892128787637526f83a4155"
        ],
        "orderId": data_order['orderId']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def acceptConnectedApprovalManager():
    '''并网发电审核'''
    url = f"{data_url}/constructmanager/acceptConnectedApprovalManager/approve"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"status": "2", "remark": None, "orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def acceptProjectAcceptanceManager():
    '''工程验收'''
    url = f"{data_url}/constructmanager/acceptProjectAcceptanceManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "constructProjectAcceptanceReport": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/169468525741277R9Io.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095417Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d17d6d4ff2384117d58c9f35edddc7936214664ea45674dd0eb83147f178c522",
        "projectDefectRectificationList": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685261648ECFc2K.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095421Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=de18e9c8fed0fffd9d92c3a6d0a0fdef5472256dbe2b9d1a01b4052f0cbb40f7",
        "projectRectificationConfirmationSheet": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685264375vMLQ4X.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095424Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=427e1809b153a91b6b41f565ac32e4274550f43f8b1ad5154e17dc125b8e3e0f",
        "engineeringData": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685259625jokhNb.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095419Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=ae6ecd1dff96ce10929b2f44cbe505f39aeabc9b6eed80ccaafcc2276017770e",
        "equipmentData": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685266069nacxz6.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095426Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d852be1f3a7dfe5287dd7383c7028ab9ff642277d749885374912c9cab4d165c",
        "gridData": [
            "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685268355dp55mt.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095428Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9c22f24eaf700df268f11e52b429c9c85b926ea3e8c3312f9e6d586152e04e72"
        ],
        "orderId": data_order['orderId']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def acceptCompleteManager():
    '''竣工图上传'''
    url = f"{data_url}/constructmanager/acceptCompleteManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "finishedDrawing": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685358901vDpCpu.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095558Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d53744501d8f63d8c6a2cc08a04e9df554b594797030925beef07b40f53f7631",
        "orderId": data_order['orderId']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def acceptCompleteApprovalManager():
    '''竣工图审核'''
    url = f"{data_url}/constructmanager/acceptCompleteApprovalManager/approve"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"status": "2", "remark": None, "orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def acceptOwnerTuvManager():
    '''业主和TUV验收'''
    url = f"{data_url}/constructmanager/acceptOwnerTuvManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "orderId": data_order['orderId'],
        "tuvDefectRectificationList": None,
        "tuvRectificationConfirmationSheet": None,
        "ownerHandoverConfirmation": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685540723NhXJ4A.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095900Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=15dec9bfbe4d4172e24e77df2b8adbc3cb572541925c8dad907baaa0872e51f8",
        "completionStatement": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685542773zGuWM5.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095902Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e5322453ada2040f3dd33444c22af5da8972af0730604bc64b7b66150c80fb45",
        "tuvAcceptanceReport": None,
        "ownerCompletionAcceptanceReport": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685545035WtLOCs.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T095905Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6c0dd2e75d113480397fdd2cd9a375de4c475c8fa32d08bfca43e16cc6a91971"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def acceptOwnerTuvApprovalManager():
    '''业主和TUV验收审核'''
    url = f"{data_url}/constructmanager/acceptOwnerTuvApprovalManager/approve"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {"status": "2", "remark": None, "orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def acceptOmManager():
    '''运维验收'''
    url = f"{data_url}/constructmanager/acceptOmManager/submit"
    headers = {
        'platform': 'CONSTRUCTMANAGER',
        'Cookie': f'partnerOperatorToken={data_order["accessToken"]}',
        'Content-Type': 'application/json',
        "accessToken": data_order["accessToken"]
    }
    payload = {
        "orderId": data_order['orderId'],
        "transferOmConfirmationForm": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685716290e1SXK9.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T100156Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6629b70a26b535ae69fe2c762b8eba8da49f5dab304c34bc48300ace26ebfbab",
        "handoverList": "http://minio-test.skyworthpv.cn/order/test1/2023/9/14/1151910717522042880/1694685719242stGuo4.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230914T100159Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=eff0d607697a5417520c7fa7ee3fe31db42be048a9647597dbb96f359b1c9d6e"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


if __name__ == '__main__':
    logen()
    constructmanager()
    projectStartApprovalManager()
    projectStartSpecificationManager()
    filingsDesignHandleManager()
    filingsDesignStageManager()
    filingsDesignApprovalManager()
    filingsArrivalPlanManager()
    filingsDrawingApprovalManager()
    # constructApplyManager()
    # constructApplyApprovalManager()
    # constructStartInsureManager()
    # constructStartManager()
    # constructStartApprovalManager()
    # '''开工确认'''
    # constructStartConfirmManager()
    # reinforceAcceptanceManager()
    # reinforceFirstApprovalManager()
    # reinforceReviewApprovalManager()
    # constructCollectInfoManager()
    # acceptConnectedManager()
    # acceptConnectedApprovalManager()
    # acceptProjectAcceptanceManager()
    # acceptCompleteManager()
    # acceptCompleteApprovalManager()
    # acceptOwnerTuvManager()
    # acceptOwnerTuvApprovalManager()
    # acceptOmManager()
