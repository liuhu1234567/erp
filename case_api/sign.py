from common.get_token import token_operator, token_erp
import requests
import unittest
import json
from common.global_variable import customize_dict
from common.do_config import host_partnership
from common.do_faker import get_number, get_phone, get_name, get_company

data_order = {}
data_order['company'] = get_company()
data_order['faker'] = get_number(8)
data_order['phone'] = get_phone()
data_order['name'] = get_name()


def chuangjian():
    """合伙运营商创建项目"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderInfo/add"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "name": data_order['company'],
        "buildMode": 2,
        "businessDeptId": "133",
        "developManagerId": "454",
        "address": data_order['company'],
        "projectCapacity": "1000.00",
        "businessOpportunityId": None,
        "province": "620000",
        "city": "621200",
        "district": "621222"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def icpvmanager():
    """清洁能源创建项目"""
    url = f"{host_partnership}/cwgf/icpvmanager/orderInfo/add"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "name": data_order['company'],
        "buildMode": 2,
        "businessDeptId": "133",
        "developManagerId": "454",
        "address": data_order['company'],
        "projectCapacity": "1000.00",
        "businessOpportunityId": None,
        "province": "620000",
        "city": "621200",
        "district": "621222"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    url = f"{host_partnership}/cwgf/icpvmanager/orderInfo/page"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "createStartTime": None,
        "createEndTime": None,
        "orderNo": None,
        "name": data_order['company'],
        "businessDeptId": None,
        "firstLevel": None,
        "secondLevel": None,
        "levelStatus": None,
        "status": "",
        "buildMode": None,
        "pageSize": 20,
        "pageNum": 1
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['orderId'] = r.json()['data']['data'][0]['id']

    url = f"{host_partnership}/cwgf/icpvmanager/orderRelatedParty/add"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "customerFileType": 2,
        "type": 1,
        "guarantorType": None,
        "assistiveOrganType": None,
        "customerFileId": "1136705129799958529"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def p1_tijiao():
    """项目资料列表"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderProjectDocumentWeb/page"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {"buildMode": None, "orderStatus": None, "documentStatus": None, "orderNo": None,
               "name": data_order['company'],
               "pageSize": 20, "pageNum": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['orderId'] = r.json()['data']['data'][0]['orderId']
    data_order['orderNo'] = r.json()['data']['data'][0]['orderNo']

    """项目资料保存产权方"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderProjectDocumentWeb/addEquity"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "step": 1,
        "id": None,
        "equityId": None,
        "licenseUrl": None,
        "constitution": None,
        "involvement": None,
        "realEstate": None,
        "construct": None,
        "ground": None,
        "construction": None,
        "workshop": None,
        "reconnaissance": None,
        "establishment": None,
        "structure": None,
        "houseThe": None,
        "rawingReport": None,
        "guarantee": None,
        "ratepaying": None,
        "finance": None,
        "appreciation": None,
        "conditionMortgage": None,
        "legalFileListY": None,
        "legalFileListN": None,
        "latestIssue": None,
        "latestIssueFin": None,
        "familyAssetsAppre": None,
        "credit": None,
        "fincalculate": None,
        "realControlY": None,
        "realControlN": None,
        "realControlCredit": None,
        "mateCardY": None,
        "mateCardN": None,
        "married": None,
        "spouseCredit": None,
        "familyAssets": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """项目资料保存用电方"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderProjectDocumentWeb/addElectricity"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "step": 1,
        "electricityId": None,
        "id": None,
        "license": None,
        "settle": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693810533861sI7S9P.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T065533Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=757ccd108ca26294d01e313d0761b18bd47313e3fa151f86d5deee92d06e1a7c",
        "description": None,
        "stationBook": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """项目资料提交"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderProjectDocumentWeb/submit"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {"orderNo": data_order['orderNo'], "orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def fengxian():
    """风险评估审核"""
    url = f"{host_partnership}/cwgf/icpvmanager/orderRiskAssess/submit"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {"orderId": data_order['orderId'], "status": 2, "remark": ""}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def chukan():
    """初勘初设获取ID"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initSurveyManager/getFactory"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {"orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['id']

    """初勘初设厂区图纸保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initSurveyManager/saveFactory"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "factorySurveyPic": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812069085TRzcmE.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T072126Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b1536d884b96f078f0a448c94fe3a5b76fcae77a7378e47888a65a18bad3e3ed",
        "masterPlanPic": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812072090MKevRq.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T072126Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=2d900f2db3b98939581717b4f3c0ed3ce7d4851bd4ef4360bde91a45ee418cfd",
        "surveyType": 1,
        "factorySurveyEgPic": [
            {
                "originalUri": "http://minio-test.skyworthpv.cn/user/test2/2023/7/28/1134511271228854272/1690538793397f3ENJL.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T072126Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=a84c92f92925840c501bb531cadf5fe1e7c89ca65a5712cb9440bc122e2945dd"
            }
        ],
        "orderId": data_order['orderId'],
        "id": data_order['id']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """初勘初设厂房信息保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initSurveyManager/savePlant"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "plantName": "测试",
        "buildType": 3,
        "isPicture": "",
        "outdoorPic": [],
        "indoorPic": [],
        "scenePic": [
            "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812652392KDcxza.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T073052Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=4cb0b6c0d077fe3bfcf4d90608e8d21fc3fdc8360fa0e6a9815a5664cb4bda87",
            "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812653098YbT5Ez.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T073053Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=fe62401c142adc7b77421fd8781996fd60ded1483d18f7d3d5709e7e888c88ab",
            "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812653583ICGQw7.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T073053Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=760f6b909bf05ff1805731bd630d65e643e0fbcbf8f282e6db4702086a606707"
        ],
        "electricalPic": None,
        "structurePic": None,
        "buildPic": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """初勘初设业务需求保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initSurveyManager/saveBusiness"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {"isQuote": 1, "isLoad": 1, "isLayout": 1, "orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """初勘初设业务需求保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initSurveyManager/saveBusiness"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {"isQuote": 1, "isLoad": 1, "isLayout": 1, "orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """初勘初设业主需求保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initSurveyManager/saveOwner"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "voltageLevel": 1,
        "gridType": "1",
        "cableType": 1,
        "videoType": 1,
        "isClean": 1,
        "isCarport": 2,
        "carportType": None,
        "isSunshine": 2,
        "sunshineType": None,
        "sunshineDesc": None,
        "powerGeneration": 2,
        "isAlone": 1,
        "isTuv": 2,
        "zbjRatio": "1",
        "zbjYear": 1,
        "carportHigh": None,
        "sunshineHigh": None,
        "carportRemark": None,
        "isFence": 2,
        "isLighting": 2,
        "lightingType": None,
        "lightingRemark": None,
        "isLadder": 2,
        "ladderType": None,
        "ladderRemark": None,
        "isEnvironment": 2,
        "isWater": 2,
        "waterRemark": None,
        "isRust": 2,
        "rustRemark": None,
        "isTile": 2,
        "tileRemark": None,
        "isBuild": 1,
        "buildRemark": None,
        "betonHigh": None,
        "otherRemark": "1",
        "isBetonHigh": 2,
        "betonRemark": None,
        "orderId": data_order['orderId']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """初勘初设工程量清单保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initDesignManager/saveDetail"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "projectCapacity": 100000,
        "fileUri": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693813386471k4oRwZ.xlsx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T074306Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=55640bd461899061f514732b026f87ab606ab87c790896896fb442e59767e8ad",
        "initDesignDetail": [
            {
                "materialCode": "N036002-000198-001",
                "materialName": "三相并网逆变器",
                "materialSort": "逆变器",
                "specification": "300K",
                "model": "SUN2000-300KTL-H0",
                "unit": "台",
                "quantity": 123,
                "installType": None
            }
        ]
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """初勘初设组件排布保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initDesignManager/saveModuleLayout"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "projectCapacity": 100000,
        "fileUri": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693813575372s2cdeJ.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T074615Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=58a5f62c1345fe800b56ff28e3ecc64ee23034bb855c902e405ecce5558783e1"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """初勘初设荷载报告保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initDesignManager/saveLoadReport"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "projectCapacity": 100000,
        "fileUri": None,
        "provideType": 1
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """初勘初设提交"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/initSurveyDesignManager/submit"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {"orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def chusheshenhe():
    """初设审核"""
    url = f"{host_partnership}/cwgf/icpvmanager/initDesignApprovalWeb/approval"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "orderNo": data_order['orderNo'],
        "status": 2,
        "remark": ""
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def yunyingshnagbaojia():
    """运营商报价提交"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/quoteQuotationInfo/update"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "detailList": [
            {
                "rowId": 2,
                "serial": "",
                "name": "光伏组件",
                "specification": "",
                "unit": "",
                "num": None,
                "price": None,
                "taxPrice": None,
                "remark": "此项由创维能源提供",
                "prowid": 1,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 3,
                "serial": "",
                "name": "逆变器",
                "specification": "",
                "unit": "",
                "num": None,
                "price": None,
                "taxPrice": None,
                "remark": "此项由创维能源提供",
                "prowid": 1,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 4,
                "serial": "",
                "name": "支架",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 1,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 6,
                "serial": "",
                "name": "低压电气设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 7,
                "serial": "",
                "name": "箱变",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 8,
                "serial": "",
                "name": "高压一次设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 9,
                "serial": "",
                "name": "高压二次设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 10,
                "serial": "",
                "name": "SVG设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 12,
                "serial": "",
                "name": "直流线缆",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 13,
                "serial": "",
                "name": "交流线缆",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 14,
                "serial": "",
                "name": "电缆桥架",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 16,
                "serial": "",
                "name": "施工辅材",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 15,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 18,
                "serial": "",
                "name": "光伏施工",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 19,
                "serial": "",
                "name": "电气设备基础",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 20,
                "serial": "",
                "name": "电网接入施工",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 22,
                "serial": "",
                "name": "清洗系统",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 21,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 23,
                "serial": "",
                "name": "导水夹",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 21,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 24,
                "serial": "",
                "name": "TUV",
                "specification": "",
                "unit": "",
                "num": None,
                "price": None,
                "taxPrice": None,
                "remark": "此项由创维能源提供",
                "prowid": 21,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 26,
                "serial": "",
                "name": "阳光棚施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 27,
                "serial": "",
                "name": "阳光棚材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 28,
                "serial": "",
                "name": "车棚施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 29,
                "serial": "",
                "name": "车棚材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 30,
                "serial": "",
                "name": "换瓦施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 31,
                "serial": "",
                "name": "换瓦材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 32,
                "serial": "",
                "name": "加固施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 33,
                "serial": "",
                "name": "加固材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 35,
                "serial": "",
                "name": "设计费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 36,
                "serial": "",
                "name": "接入批复",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 37,
                "serial": "",
                "name": "工程保险",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 38,
                "serial": "",
                "name": "安全文明施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 39,
                "serial": "",
                "name": "项目管理费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            }
        ]
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def lixiangshenpi():
    """立项审批获取id"""
    url = f"{host_partnership}/cwgf/icpvmanager/projectApprovalManager/get"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {"orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['project_id'] = r.json()['data']['id']

    """立项审批保存"""
    url = f"{host_partnership}/cwgf/icpvmanager/projectApprovalManager/update"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "upperLimit": 10,
        "quotationRemark": None,
        "companyName": "测试",
        "attachmentUri": None,
        "details": [
            {
                "rowId": 2,
                "serial": "",
                "name": "光伏组件",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "此项由创维能源提供",
                "prowid": 1,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 3,
                "serial": "",
                "name": "逆变器",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "此项由创维能源提供",
                "prowid": 1,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 4,
                "serial": "",
                "name": "支架",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 1,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 6,
                "serial": "",
                "name": "低压电气设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 7,
                "serial": "",
                "name": "箱变",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 8,
                "serial": "",
                "name": "高压一次设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 9,
                "serial": "",
                "name": "高压二次设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 10,
                "serial": "",
                "name": "SVG设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 12,
                "serial": "",
                "name": "直流线缆",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 13,
                "serial": "",
                "name": "交流线缆",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 14,
                "serial": "",
                "name": "电缆桥架",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 16,
                "serial": "",
                "name": "施工辅材",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 15,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 18,
                "serial": "",
                "name": "光伏施工",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 19,
                "serial": "",
                "name": "电气设备基础",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 20,
                "serial": "",
                "name": "电网接入施工",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 22,
                "serial": "",
                "name": "清洗系统",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 21,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 23,
                "serial": "",
                "name": "导水夹",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 21,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 24,
                "serial": "",
                "name": "TUV",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "此项由创维能源提供",
                "prowid": 21,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 26,
                "serial": "",
                "name": "阳光棚施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 27,
                "serial": "",
                "name": "阳光棚材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 28,
                "serial": "",
                "name": "车棚施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 29,
                "serial": "",
                "name": "车棚材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 30,
                "serial": "",
                "name": "换瓦施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 31,
                "serial": "",
                "name": "换瓦材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 32,
                "serial": "",
                "name": "加固施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 33,
                "serial": "",
                "name": "加固材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 35,
                "serial": "",
                "name": "设计费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 36,
                "serial": "",
                "name": "接入批复",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 37,
                "serial": "",
                "name": "工程保险",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 38,
                "serial": "",
                "name": "安全文明施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 39,
                "serial": "",
                "name": "项目管理费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            }
        ]
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """立项审批提交"""
    url = f"{host_partnership}/cwgf/icpvmanager/projectApprovalManager/submit"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {"orderId": data_order['orderId'], "status": 2, "approveRemark": None}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def suodanliebioa():
    """锁单列表提交"""
    url = f"{host_partnership}/cwgf/icpvmanager/orderLock/submit"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "epcUri": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/16938152252477uXRj4.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T081345Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=18235172940f0d4ecb8635e8d5565c5b89bacf8876556f76017c3232230cf8cf",
        "emcUri": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/16938152252477uXRj4.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T081345Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=18235172940f0d4ecb8635e8d5565c5b89bacf8876556f76017c3232230cf8cf",
        "others": [
            {
                "otherFileUri": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693815230737CAcuf1.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T081350Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6744fd281cb2dab6225451c1a152929a3d6cdb91cafdc446a35fbde895294973",
                "serialNo": 0
            }
        ]
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def xiangkan():
    """详勘厂区图纸保存"""
    url = f"{host_partnership}/cwgf/icpvmanager/detailSurveyManager/saveFactory"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "detailSurveyTotalLayoutPicUri": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136662679625490432/1693815486653mc7JIQ.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T081806Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=bec23d28cc6186a9838d312a077cd5a5e04e536f6a4f966eb27a2f462321da32",
        "surveyType": 1,
        "orderId": data_order['orderId']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """详勘厂房信息获取ID"""
    url = f"{host_partnership}/cwgf/icpvmanager/detailSurveyManager/listPlant"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {"orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['detail_data'] = r.json()['data']['data'][0]['id']

    """详勘厂房信息保存"""
    url = f"{host_partnership}/cwgf/icpvmanager/detailSurveyManager/updatePlant"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "surveyType": 1,
        "plantName": "测试",
        "buildType": 3,
        "isPicture": None,
        "indoorPic": [],
        "planeLayoutPic": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/16938156825003V8AHd.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T082122Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e58485e960c6d3d7cb597bf88b7f41f90dba43ff6040895267ca4fc7eebe76be",
        "scenePic": [
            "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812652392KDcxza.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T082117Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=c7025ef1dff83e66514e76c3f8da32c6a9244012adf43f560eb4f3ea6cc7f9a0",
            "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812653098YbT5Ez.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T082117Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=82c830f1feb7999a9d625af98ec3ae216067de648600223faad554b3a918587c",
            "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812653583ICGQw7.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T082117Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9c16cc992d1b1f8c9f137ecad0ce7a3b33e804b60641bc12161a5009e47068d0"
        ],
        "indoorRoofPanoramicViewPic": [],
        "indoorSuspendedCeilingOrHangingPic": [],
        "id": data_order['detail_data']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """详勘配电室保存"""
    url = f"{host_partnership}/cwgf/icpvmanager/detailSurveyManager/savePdRoom"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "name": "测试",
        "level": 1,
        "lineLevel": 1,
        "lineLoop": 1,
        "loopName": "测试",
        "isCompensate": 2,
        "switchyardLayoutPic": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693816170727dDR3LS.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T082930Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=84e1ce53d0446ef1695205a104ddc3bcc2f64f301e7f1429bb323ed93659ab27",
        "reserveTankPic": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693816158164svgf7o.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T082918Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f4a6c81af499194c48ba8efac6db246fb5719e8e0c95391cbb7f397c030a70f3",
        "lineProtectiveDevicesPic": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693816172648v2tfQi.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T082932Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=146776197be935f0a6edc236652fe2f64b8badcb8f45c3c586ed1cc4fb7e87ce",
        "factoryPrimaryWiringPic": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693816160834dycr9j.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T082920Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=fba9950b6e30ccaa2bc7b2dd3f89ef86e3861ef46160a91ceb368b1c5d5c29d0",
        "plane": "",
        "installed": "",
        "nameOneUri": "",
        "nameTwoUri": "",
        "pdTransformer": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """详勘提交"""
    url = f"{host_partnership}/cwgf/icpvmanager/detailSurveyManager/submit"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {"orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def chushefuhe():
    """初设复核提交"""
    url = f"{host_partnership}/cwgf/icpvmanager/finalDesignAuditManager/submit"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {"orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def yunyingshanghejia():
    """运营商核价获取ID"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/quotePricingInfo/getDetailByOrderId/{data_order['orderId']}"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    r = requests.get(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    data_order['getDetail'] = r.json()['data']['id']

    """运营商核价提交"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/quotePricingInfo/update"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "detailList": [
            {
                "rowId": 2,
                "serial": "",
                "name": "光伏组件",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "此项由创维能源提供",
                "prowid": 1,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 3,
                "serial": "",
                "name": "逆变器",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "此项由创维能源提供",
                "prowid": 1,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 4,
                "serial": "",
                "name": "支架",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 1,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 6,
                "serial": "",
                "name": "低压电气设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 7,
                "serial": "",
                "name": "箱变",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 8,
                "serial": "",
                "name": "高压一次设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 9,
                "serial": "",
                "name": "高压二次设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 10,
                "serial": "",
                "name": "SVG设备",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 12,
                "serial": "",
                "name": "直流线缆",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 13,
                "serial": "",
                "name": "交流线缆",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 14,
                "serial": "",
                "name": "电缆桥架",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 16,
                "serial": "",
                "name": "施工辅材",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 15,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 18,
                "serial": "",
                "name": "光伏施工",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 19,
                "serial": "",
                "name": "电气设备基础",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 20,
                "serial": "",
                "name": "电网接入施工",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 22,
                "serial": "",
                "name": "清洗系统",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 21,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 23,
                "serial": "",
                "name": "导水夹",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 21,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 24,
                "serial": "",
                "name": "TUV",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "此项由创维能源提供",
                "prowid": 21,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 26,
                "serial": "",
                "name": "阳光棚施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 27,
                "serial": "",
                "name": "阳光棚材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 28,
                "serial": "",
                "name": "车棚施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 29,
                "serial": "",
                "name": "车棚材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 30,
                "serial": "",
                "name": "换瓦施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 31,
                "serial": "",
                "name": "换瓦材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 32,
                "serial": "",
                "name": "加固施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 33,
                "serial": "",
                "name": "加固材料费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 35,
                "serial": "",
                "name": "设计费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 36,
                "serial": "",
                "name": "接入批复",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 37,
                "serial": "",
                "name": "工程保险",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 38,
                "serial": "",
                "name": "安全文明施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 39,
                "serial": "",
                "name": "项目管理费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            }
        ]
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def p2zhiliao():
    """项目资料P2阶段产权方获取ID"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderProjectDocumentWeb/getDetail"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {"orderId": data_order['orderId'], "step": 2, "documentType": "2"}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['equityId'] = r.json()['data']['equityData']['id']

    """项目资料P2阶段产权方保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderProjectDocumentWeb/updateEquity"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "step": 2,
        "id": data_order['equityId'],
        "equityId": data_order['equityId'],
        "licenseUrl": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693817487139vFSFIb.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T085127Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=55d5ef1747cb9109df0e7d4165e8ee830a9ffee4da73fbfcaac127522bfe771f",
        "constitution": None,
        "involvement": None,
        "realEstate": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/16938174896039aoZzC.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T085129Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=af61ec9dca3b0d86e1426665f7b89c9f6276de19ed8c0e6efb20cb523291777f",
        "construct": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693817493806RLFMKg.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T085133Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=01b877641f96f508936c7d250d9b0794eeaf29fe3fc2a62b87ac9f974ffd7df6",
        "ground": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693817502512mxOrao.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T085142Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f7b8ab42a2595f4b2d7bb0c8195660732488c88caa70f9135fa6401142f8fc9c",
        "construction": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693817506553CPDckW.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T085146Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=eec886e340e885f12b5ea567b19fc261eda1d23fd692a021b14b7d85af5381d5",
        "workshop": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136662679625490432/1693815486653mc7JIQ.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T085114Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=284c94ad149564ccd87e6feaaf04c6d9b0fb574e8caee33e1048901c4c2b7502",
        "reconnaissance": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812069085TRzcmE.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T085114Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8ced42abaf2fd758e6b97cd57da971ec5326d8d4735fccb7d52861aa526bd82a",
        "establishment": None,
        "structure": None,
        "houseThe": None,
        "rawingReport": None,
        "guarantee": None,
        "ratepaying": None,
        "finance": None,
        "appreciation": None,
        "conditionMortgage": None,
        "legalFileListY": None,
        "legalFileListN": None,
        "latestIssue": None,
        "latestIssueFin": None,
        "familyAssetsAppre": None,
        "credit": None,
        "fincalculate": None,
        "realControlY": None,
        "realControlN": None,
        "realControlCredit": None,
        "mateCardY": None,
        "mateCardN": None,
        "married": None,
        "spouseCredit": None,
        "familyAssets": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """项目资料P2阶段产权方获取ID"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderProjectDocumentWeb/getDetail"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {"orderId": data_order['orderId'], "step": 2, "documentType": "3"}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['electricityId'] = r.json()['data']['electricityData']['id']

    """项目资料P2阶段用电方保存"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderProjectDocumentWeb/updateElectricity"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {
        "orderId": data_order['orderId'],
        "step": 2,
        "electricityId": data_order['electricityId'],
        "id": data_order['electricityId'],
        "license": None,
        "settle": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693810533861sI7S9P.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T090210Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d0c219554c5f1ee69705e10b95555d6d8bd4e118b528a4b6ff0e060e0955fc39",
        "description": None,
        "stationBook": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """项目资料P2阶段提交"""
    url = f"{host_partnership}/cwgf/icpvoperatormanager/orderProjectDocumentWeb/submit"
    headers = {
        'platform': 'ICPVOPERATORMANAGER',
        'Cookie': f'partnerOperatorToken={token_operator}',
        'Content-Type': 'application/json',
        "accessToken": token_operator
    }
    payload = {"orderNo": data_order['orderNo'], "orderId": data_order['orderId']}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def qianyezhiliao():
    """签约资料审核-签约模板上传保存"""
    url = f"{host_partnership}/cwgf/icpvmanager/signFileApprove/addTemplate"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "emcUri": None,
        "epcUri": "http://minio-test.skyworthpv.cn/user/test2/2023/9/6/1136662679625490432/1693979171382W6vKEe.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230906T054611Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=b4369dbaa47ef368760d5cfd8967871533c3ea44b0be6c591fe6d7a8de505ebe",
        "financeLeaseUri": None,
        "subpackageUri": "http://minio-test.skyworthpv.cn/user/test2/2023/9/6/1136662679625490432/1693979174156UVwsr8.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230906T054614Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=86da497c0e0173c73e53edbdd42a632bc18ad047718623ab53154babf4d446cd",
        "supplements": None,
        "others": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """新建合作客户"""
    url = f"{host_partnership}/cwgf/icpvmanager/customerFileBaseInfo/customerAdd"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "id": None,
        "customerName": f"测试{data_order['faker']}",
        "uscCode": f"{data_order['faker']}088140947F",
        "province": "620000",
        "city": "621200",
        "district": "621222",
        "address": "广州省深圳市保安区松白路玉山公寓2030栋314",
        "lpName": None,
        "lpPhone": None,
        "lpIdCard": None,
        "cisAc": 0,
        "acName": None,
        "acPhone": None,
        "acIdCard": None,
        "contactName": data_order['name'],
        "contactPhone": data_order['phone'],
        "contactIdCard": None,
        "contactPosition": None,
        "userAccount": data_order['phone'],
        "userName": data_order['name'],
        "expStartDate": None,
        "expDate": None,
        "performBondDate": None,
        "qualType": None,
        "businessDeptId": None,
        "developManagerId": None,
        "remark": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['datas'] = r.json()['data']

    """签约资料审核-关联用电方公司"""
    url = f"{host_partnership}/cwgf/icpvmanager/orderRelatedParty/add"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "customerFileType": 1,
        "type": 4,
        "guarantorType": None,
        "assistiveOrganType": None,
        "customerFileId": data_order['datas']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """签约资料审核-关联产权方公司"""
    url = f"{host_partnership}/cwgf/icpvmanager/orderRelatedParty/add"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "customerFileType": 1,
        "guarantorType": None,
        "assistiveOrganType": None,
        "type": 3,
        "customerFileId": data_order['datas']
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """签约资料审核-关联签约甲方公司"""
    url = f"{host_partnership}/cwgf/icpvmanager/orderRelatedParty/add"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "customerFileType": 1,
        "type": 2,
        "guarantorType": None,
        "assistiveOrganType": None,
        "customerFileId": '1136704289475346433'
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """签约资料审核-获取项目资料清单ID"""
    url = f"{host_partnership}/cwgf/icpvmanager/orderProjectDocumentWeb/getDetail"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {"orderId": data_order['orderId'], "step": 2, "documentType": "2"}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['equityId'] = r.json()['data']['equityData']['id']

    """签约资料审核-项目资料清单保存"""
    url = f"{host_partnership}/cwgf/icpvmanager/orderProjectDocumentWeb/updateEquity"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "step": 2,
        "id": data_order['equityId'],
        "equityId": data_order['equityId'],
        "licenseUrl": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693817487139vFSFIb.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T094852Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=762573e94def16b4b68c022d5684355ebee924cc388ca2a009731a7e0b0298cc",
        "constitution": None,
        "involvement": None,
        "realEstate": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/16938174896039aoZzC.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T094852Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6078aea2299c9c0e083e15e988e97f66d0c41a8672dc05eac7714022300c79b3",
        "construct": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693817493806RLFMKg.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T094852Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=93c61a35d18e0903784318dd31f02da02ef9d5722e2ca988433e250699f1d0ee",
        "ground": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693817502512mxOrao.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T094852Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6b26b81a12b60ec332331f2a1b232e5111ee0cffefae440943a829126c57613d",
        "construction": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136705129895256064/1693817506553CPDckW.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T094852Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=2545992dacc05d0ca5261cc1abce606ad8000fbcdf1e83d8c76aa9b82ab4a284",
        "workshop": "http://minio-test.skyworthpv.cn/user/test2/2023/9/4/1136662679625490432/1693815486653mc7JIQ.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T094852Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=13156e17c865a06b54449b406f6b892e896ffaf4080a6e89c3e5539f8845f66e",
        "reconnaissance": "http://minio-test.skyworthpv.cn/order/test2/2023/9/4/1148275314759819264/1693812069085TRzcmE.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230904T094852Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e63e2b7f18e86b580874629d6a61f16c554a92aca7187fee27289af716844db7",
        "establishment": None,
        "structure": None,
        "houseThe": None,
        "rawingReport": None,
        "guarantee": None,
        "ratepaying": None,
        "finance": None,
        "appreciation": None,
        "conditionMortgage": None,
        "legalFileListY": None,
        "legalFileListN": None,
        "latestIssue": None,
        "latestIssueFin": None,
        "familyAssetsAppre": None,
        "credit": None,
        "fincalculate": None,
        "realControlY": None,
        "realControlN": None,
        "realControlCredit": None,
        "mateCardY": None,
        "mateCardN": None,
        "married": None,
        "spouseCredit": None,
        "familyAssets": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """签约资料审核-运营商核价确认保存"""
    url = f"{host_partnership}/cwgf/icpvmanager/signFileApprove/updateQuote"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "orderId": data_order['orderId'],
        "companyName": "测试",
        "upperLimit": 10000,
        "quotationRemark": None,
        "attachmentUri": None,
        "details": [
            {
                "rowId": 2,
                "serial": "",
                "name": "光伏组件",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 1,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 3,
                "serial": "",
                "name": "逆变器",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 1,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 4,
                "serial": "",
                "name": "支架",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 7000,
                "taxPrice": 700000000,
                "remark": "",
                "prowid": 1,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 6,
                "serial": "",
                "name": "低压电气设备",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 7,
                "serial": "",
                "name": "箱变",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 8,
                "serial": "",
                "name": "高压一次设备",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 9,
                "serial": "",
                "name": "高压二次设备",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 10,
                "serial": "",
                "name": "SVG设备",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 5,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 12,
                "serial": "",
                "name": "直流线缆",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 10000,
                "taxPrice": 1000000000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 13,
                "serial": "",
                "name": "交流线缆",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 6000,
                "taxPrice": 600000000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 14,
                "serial": "",
                "name": "电缆桥架",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 11,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 16,
                "serial": "",
                "name": "施工辅材",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 15,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 18,
                "serial": "",
                "name": "光伏施工",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 19,
                "serial": "",
                "name": "电气设备基础",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 20,
                "serial": "",
                "name": "电网接入施工",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 2000,
                "taxPrice": 200000000,
                "remark": "",
                "prowid": 17,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 22,
                "serial": "",
                "name": "清洗系统",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 21,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 23,
                "serial": "",
                "name": "导水夹",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 21,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 24,
                "serial": "",
                "name": "TUV",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1,
                "taxPrice": 100000,
                "remark": "",
                "prowid": 21,
                "editableLevel": 2,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 26,
                "serial": "",
                "name": "阳光棚施工费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 27,
                "serial": "",
                "name": "阳光棚材料费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 28,
                "serial": "",
                "name": "车棚施工费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 29,
                "serial": "",
                "name": "车棚材料费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 30,
                "serial": "",
                "name": "换瓦施工费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 31,
                "serial": "",
                "name": "换瓦材料费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 32,
                "serial": "",
                "name": "加固施工费",
                "specification": "",
                "unit": "",
                "num": None,
                "price": 7000,
                "taxPrice": 700000000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 33,
                "serial": "",
                "name": "加固材料费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 25,
                "editableLevel": 1,
                "required": 0,
                "level": 2,
                "children": None
            },
            {
                "rowId": 35,
                "serial": "",
                "name": "设计费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 36,
                "serial": "",
                "name": "接入批复",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 37,
                "serial": "",
                "name": "工程保险",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 38,
                "serial": "",
                "name": "安全文明施工费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            },
            {
                "rowId": 39,
                "serial": "",
                "name": "项目管理费",
                "specification": "",
                "unit": "",
                "num": 1000,
                "price": 1000,
                "taxPrice": 100000000,
                "remark": "",
                "prowid": 34,
                "editableLevel": 1,
                "required": 1,
                "level": 2,
                "children": None
            }
        ]
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')

    """签约资料审核提交"""
    url = f"{host_partnership}/cwgf/icpvmanager/signFileApprove/submit"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {"orderId": data_order['orderId'], "status": 2, "remark": ""}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def jiafangshenhe():
    """清洁能源登录-获取验证码"""
    url = "http://spvpre-gateway.skyworthpv.cn/public/verifyCode/calculate"
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
    data_order['imgKey'] = r.json()['data']['imgKey']
    data_order['imgValue'] = r.json()['data']['imgValue']

    url = "http://spvpre-gateway.skyworthpv.cn/public/sendSms"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': "ICPVOWNER",
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    payload = {"verifyCodeObj": {"key": data_order['imgKey'], "verifyCode": data_order['imgValue']},
               "phone": '17585245511', "type": 1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['sendSms'] = r.json()['data']

    url = "http://spvpre-gateway.skyworthpv.cn/login"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'platform': "ICPVOWNER",
        'Cookie': 'sidebarStatus=0',
        'Content-Type': 'application/json',
    }
    payload = {"username": '17585245511', "code": data_order['sendSms'], "type": 2}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    accessToken = r.json()['data']['accessToken']

    """甲方审核通过"""
    url = "http://spvpre-gateway.skyworthpv.cn/icpvowner/orderOwnerApprove/confirm"
    headers = {
        'platform': 'ICPVOWNER',
        'Cookie': f'partnerOperatorToken={accessToken}',
        'Content-Type': 'application/json',
        "accessToken": accessToken
    }
    payload = {"orderId": data_order['orderId'], "status": 2}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


def qianyue():
    """签约列表获取id"""
    url = f"{host_partnership}/cwgf/icpvmanager/signInfoManager/detail/{data_order['orderId']}"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    data_order['id'] = r.json()['data']['id']

    """签约列表上传资料"""
    url = f"{host_partnership}/cwgf/icpvmanager/signInfoManager/uploadFile"
    headers = {
        'platform': 'ICPVMANAGER',
        'Cookie': f'partnerOperatorToken={token_erp}',
        'Content-Type': 'application/json',
        "accessToken": token_erp
    }
    payload = {
        "id": data_order['id'],
        "orderId": data_order['orderId'],
        "oaNumber": data_order['faker'],
        "gridLevel": 2,
        "EMCContractUri": None,
        "EPCContractUri": "http://minio-test.skyworthpv.cn/user/test2/2023/9/5/1136662679625490432/16938805281680MTg3F.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230905T022208Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=89889957e293b84dd3ec9f0df88a48569d11ca8ce8ba5851f0ff09f6ea1130ef",
        "financeLeaseContractUri": None,
        "engineeringSubcontractUri": "http://minio-test.skyworthpv.cn/user/test2/2023/9/5/1136662679625490432/1693880530865gXuHVU.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin%2F20230905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230905T022210Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=5104fa64b7372e04f763b919da2aaaad8591798b1809982acf139a692b3ac6c0",
        "supplementaryAgreementUri": None,
        "othersUri": None
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')


if __name__ == '__main__':
    """新建项目"""
    # chuangjian()
    icpvmanager()
    """p1阶段提交"""
    p1_tijiao()
    """风险评估"""
    fengxian()
    """初勘初设"""
    chukan()
    """初设审核"""
    chusheshenhe()
    """运营商报价"""
    yunyingshnagbaojia()
    """立项审批"""
    lixiangshenpi()
    """锁单列表"""
    suodanliebioa()
    """详勘"""
    xiangkan()
    """初设复核"""
    chushefuhe()
    """运营商核价"""
    yunyingshanghejia()
    """p2阶段资料提交"""
    p2zhiliao()
    """签约资料审核"""
    qianyezhiliao()
    """甲方审核"""
    jiafangshenhe()
    """签约"""
    qianyue()
