# from common.do_config import api_host, restime
# from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
#     token_scf_subsidiaries, token_scf_enterprise
# from common.global_variable import customize_dict
# from common.do_faker import get_company, get_number, get_name, get_phone, get_email, get_money
# from common.do_excel import DoExcel
# from common.do_time import time_format
# from case_api.template import api_template_uploadfile
# from case_api.enterprise import api_enterprise_queryEntArchivesDetail
# import requests
# import unittest
# import json
# import time
# import datetime
#
# """金点信"""
#
#
# def api_goldenLetter_open_deleteBillTempById(token, payload):
#     """根据id删除发票"""
#     url = f'{api_host}/api-scf/goldenLetter/open/deleteBillTempById'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_open_importBillExcel(token, payload):
#     """开立-导入发票"""
#     url = f'{api_host}/api-scf/goldenLetter/open/importBillExcel'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_open_insert(token, payload):
#     """开立新增"""
#     url = f'{api_host}/api-scf/goldenLetter/open/insert'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token,
#         "x-userid-header": "1562325610995245058"
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_open_queryPage(token, payload):
#     """查询开立审核列表"""
#     url = f'{api_host}/api-scf/goldenLetter/open/queryPage'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_open_updateAuditStatus(token, payload):
#     """开立审核"""
#     url = f'{api_host}/api-scf/goldenLetter/open/updateAuditStatus'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_queryBillList(token, payload):
#     """开立-查询发票-临时表"""
#     url = f'{api_host}/api-scf/goldenLetter/queryBillList'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_queryBillListById(token, payload):
#     """根据金点信ID查询发票详情"""
#     url = f'{api_host}/api-scf/goldenLetter/queryBillListById'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_queryByCode(token, payload):
#     """根据code查询金点信详情"""
#     url = f'{api_host}/api-scf/goldenLetter/queryByCode'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_queryById(token, payload):
#     """根据ID查询金点信详情"""
#     url = f'{api_host}/api-scf/goldenLetter/queryById'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_queryConfigSet(token, payload):
#     """根据核心企业id查询开立基础项配置"""
#     url = f'{api_host}/api-scf/goldenLetter/queryConfigSet'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_queryPage(token, payload):
#     """查询金点信列表"""
#     url = f'{api_host}/api-scf/goldenLetter/queryPage'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_resubmit(token, payload):
#     """重新提交"""
#     url = f'{api_host}/api-scf/goldenLetter/resubmit'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_retrospective(token, payload):
#     """金点信追溯"""
#     url = f'{api_host}/api-scf/goldenLetter/retrospective'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_getCreditAmount(token, payload):
#     """获取授信额度"""
#     url = f'{api_host}/api-scf/goldenLetter/getCreditAmount'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_open_deleteBillTemp(token, payload):
#     """删除全部导入的发票"""
#     url = f'{api_host}/api-scf/goldenLetter/open/deleteBillTemp'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_selectProject(token, payload):
#     """查询融资项目"""
#     url = f'{api_host}/api-scf/goldenLetter/selectProject'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def insert_excel_importCustomerFromExcel(num):
#     excel = DoExcel('导入发票模板.xlsx', '普票')
#     for n in range(num):
#         row_value = (
#             '普票',
#             get_number(10),
#             get_number(8),
#             datetime.date(2022, 9, 2),
#             '91440300279446850J',
#             '91320600673032592M',
#             get_number(6),
#             get_money(4)
#         )
#         excel.insert(row_value, 3 + n)
#     file_name = excel.save()
#     return file_name
#
#
# def api_goldenLetter_open_getGoldenLetterCode(token, payload):
#     """开立新增界面生成金点信编号"""
#     url = f'{api_host}/api-scf/goldenLetter/open/getGoldenLetterCode'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_open_preview(token, payload):
#     """金点信预览"""
#     url = f'{api_host}/api-scf/goldenLetter/open/preview'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_queryPdfById(token, payload):
#     """根据ID查询金点信pdf详情"""
#     url = f'{api_host}/api-scf/goldenLetter/queryPdfById'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_getBusType(token, payload):
#     """判断审批类型"""
#     url = f'{api_host}/api-scf/goldenLetter/getBusType'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_goldenLetterOpenSeal(token, payload):
#     """金点信开立平台方审核签章返回地址"""
#     url = f'{api_host}/api-scf/goldenLetter/goldenLetterOpenSeal'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# def api_goldenLetter_updateGoldenLetterAddress(token, payload):
#     """签章后更新文件地址"""
#     url = f'{api_host}/api-scf/goldenLetter/updateGoldenLetterAddress'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r
#
#
# g_d = {}
#
#
# class GoldenLetter(unittest.TestCase):
#     def test_001_goldenLetter_open_getGoldenLetterCode(self):
#         """开立新增界面生成金点信编号"""
#         payload = {
#         }
#         r = api_goldenLetter_open_getGoldenLetterCode(token_scf_enterprise, payload)
#         r_json = r.json()
#         g_d["goldenLetterCode"] = r_json["datas"]
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_002_goldenLetter_open_importBillExcel(self):
#         """开立-导入发票"""
#         file_name = insert_excel_importCustomerFromExcel(1)
#         path = api_template_uploadfile(token_scf_platform, file_name).json()["datas"]["path"]
#         fileId_new = "group1/" + path
#         payload = {
#             "fileId": fileId_new
#         }
#         r = api_goldenLetter_open_importBillExcel(token_scf_enterprise, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_003_goldenLetter_open_insert(self):
#         """开立新增 V2.1.1修改"""
#         g_d["coreEntId"] = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()["datas"]["id"]
#         g_d["recipientId"] = api_enterprise_queryEntArchivesDetail(token_scf_supplier).json()["datas"]["id"]
#         payload = {
#             "bills": ["1562284267547848706", "1562284267556237314"],
#             "coreEntId": g_d.get("coreEntId"),
#             "coreEntName": "核心企业",
#             "creditEnhancerId": 1544611013257465857,
#             "creditEnhancerName": "西咸新区沣东新城一",
#             "founderEnt": "核心企业",
#             "founderEntId": g_d.get("coreEntId"),
#             "goldenLetterCode": g_d.get("goldenLetterCode"),
#             "goldenLetterEndDate": "2024-07-09T14:00:00",
#             "goldenLetterMoney": 1000,
#             "goldenLetterOpenDate": "2023-07-09T10:00:00",
#             "invoiceAmountProportion": "100%",
#             "invoiceWithTax": 1000,
#             "orderName": "合同/订单名称",
#             "orderNumber": "合同/订单编号",
#             "promisedPaymentDate": "2023-07-09T10:00:00",
#             "recipient": "供应商",
#             "recipientId": g_d.get("recipientId"),
#             "remainingAvailableQuota": 0,
#             "remainingOpenableInvoice": 0,
#             "statementNumber": "对账单编号",
#             "totalIssuerQuota": 1000,
#             "usedQuota": 1000
#         }
#         r = api_goldenLetter_open_insert(token_scf_enterprise, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_004_open_queryPage(self):
#         """查询开立审核列表"""
#         payload = {
#             "auditStatus": 1,
#             "founderEnt": "",
#             "goldenLetterCode": "",
#             "num": 1,
#             "recipient": "",
#             "size": 10
#         }
#         r = api_goldenLetter_open_queryPage(token_scf_enterprise, payload)
#         r_json = r.json()
#         g_d["id"] = r_json["datas"][0]["id"]
#         g_d["auditFlowItemId"] = r_json["datas"][0]["auditFlowItemId"]
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_005_goldenLetter_queryById(self):
#         """根据ID查询金点信详情"""
#         payload = {
#             "id": g_d.get("id")
#         }
#         r = api_goldenLetter_queryById(token_scf_platform, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_006_goldenLetter_queryBillList(self):
#         """开立-查询发票-临时表"""
#         payload = {
#             "coreEntName": "欣旺达",
#             "date": "2022-07",
#             "division": "电池事业部",
#             "recipient": "AAA公司"
#         }
#         r = api_goldenLetter_queryBillList(token_scf_platform, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_007_goldenLetter_queryBillListById(self):
#         """根据金点信ID查询发票详情"""
#         payload = {
#             "id": 1562699313327308802
#         }
#         r = api_goldenLetter_queryBillListById(token_scf_platform, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_008_goldenLetter_queryByCode(self):
#         """根据code查询金点信详情"""
#         payload = {
#             "goldenLetterCode": "",
#             "num": 1,
#             "size": 10
#         }
#         r = api_goldenLetter_queryByCode(token_scf_platform, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_009_goldenLetter_open_updateAuditStatus(self):
#         """开立审核 V2.1.1修改"""
#         payload = {
#             "auditEntId": g_d.get("coreEntId"),
#             "auditFlowItemId": g_d.get("auditFlowItemId"),
#             "auditOpinion": "",
#             "auditStatus": 3,
#             "busType": "",
#             "coreEntId": g_d.get("coreEntId"),
#             "creditEnhancerId": 0,
#             "entId": g_d.get("coreEntId"),
#             "id": g_d.get("id"),
#             "projectId": 0,
#             "recipientId": g_d.get("recipientId")
#         }
#         r = api_goldenLetter_open_updateAuditStatus(token_scf_enterprise, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_010_goldenLetter_queryConfigSet(self):
#         """根据核心企业id查询开立基础项配置"""
#         Id = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()["datas"]["id"]
#         payload = {
#             "id": Id
#         }
#         r = api_goldenLetter_queryConfigSet(token_scf_platform, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_011_goldenLetter_queryPage(self):
#         """查询金点信列表"""
#         payload = {
#             "auditStatus": 1,
#             "currentHolder": "",
#             "founderEnt": "",
#             "goldenLetterCode": "",
#             "num": 1,
#             "paymentStatus": 0,
#             "size": 10
#         }
#         r = api_goldenLetter_queryPage(token_scf_platform, payload)
#         r_json = r.json()
#         g_d["goldenLetterId"] = r_json["datas"][0]["id"]
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_012_goldenLetter_resubmit(self):
#         """重新提交"""
#         company = get_company()
#         payload = {
#             "auditFlowItemId": g_d.get("auditFlowItemId"),
#             "bills": ["1562284267547848706", "1562284267556237314"],
#             "coreEntId": g_d.get("coreEntId"),
#             "coreEntName": "核心企业",
#             "creditEnhancerId": 0,
#             "creditEnhancerName": company,
#             "currentHolder": "",
#             "currentHolderId": 0,
#             "founderEnt": company,
#             "founderEntId": 0,
#             "goldenLetterCode": "金电信编号",
#             "goldenLetterEndDate": "2018-07-09T14:00:00",
#             "goldenLetterMoney": 0,
#             "goldenLetterOpenDate": "2018-07-09T10:00:00",
#             "id": 0,
#             "initialHolder": "",
#             "initialHolderId": 0,
#             "invoiceAmountProportion": "发票开立金额比例",
#             "invoiceWithTax": 0,
#             "openApplicationNumber": "开立申请编号",
#             "orderName": "合同/订单名称",
#             "orderNumber": "合同/订单编号",
#             "promisedPaymentDate": "2018-07-09T14:00:00",
#             "recipient": company,
#             "recipientId": 0,
#             "remainingAvailableQuota": 0,
#             "remainingOpenableInvoice": 0,
#             "statementNumber": "对账单编号",
#             "totalIssuerQuota": 0,
#             "usedQuota": 0
#         }
#         r = api_goldenLetter_resubmit(token_scf_enterprise, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_013_goldenLetter_getCreditAmount(self):
#         """获取授信额度"""
#         payload = {
#             "id": 1549684806067781633
#         }
#         r = api_goldenLetter_getCreditAmount(token_scf_platform, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_014_goldenLetter_open_deleteBillTemp(self):
#         """删除全部导入的发票"""
#         payload = {
#         }
#         r = api_goldenLetter_open_deleteBillTemp(token_scf_platform, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_015_goldenLetter_selectProject(self):
#         """查询融资项目"""
#         payload = {
#         }
#         r = api_goldenLetter_selectProject(token_scf_platform, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_016_goldenLetter_open_deleteBillTempById(self):
#         """根据id删除发票"""
#         payload = {
#             "id": 0
#         }
#         r = api_goldenLetter_open_deleteBillTempById(token_scf_enterprise, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     ###接口还没弄好，2022-9-6
#     # def test_017_goldenLetter_open_preview(self):
#     #     """金点信预览"""
#     #     payload = {
#     #         "coreEntName": "",
#     #         "creditEnhancerName": "",
#     #         "founderEnt": "",
#     #         "goldenLetterCode": "",
#     #         "goldenLetterEndDate": "",
#     #         "goldenLetterMoney": 0,
#     #         "goldenLetterOpenDate": "",
#     #         "orderName": "",
#     #         "orderNumber": "",
#     #         "promisedPaymentDate": "",
#     #         "recipient": "",
#     #         "remainingAvailableQuota": 0,
#     #         "statementNumber": "",
#     #         "totalIssuerQuota": 0,
#     #         "usedQuota": 0
#     #     }
#     #     r = api_goldenLetter_open_preview(token_scf_enterprise, payload)
#     #     r_json = r.json()
#     #     restime_now = r.elapsed.total_seconds()
#     #     customize_dict['restime_now'] = restime_now
#     #     self.assertEqual(200, r_json['resp_code'])
#     #     self.assertEqual('SUCCESS', r_json['resp_msg'])
#     #     self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     ###接口已删除
#     # def test_018_goldenLetter_queryPdfById(self):
#     #     """根据ID查询金点信pdf详情"""
#     #     payload = {
#     #         "id": 0
#     #     }
#     #     r = api_goldenLetter_queryPdfById(token_scf_enterprise, payload)
#     #     r_json = r.json()
#     #     restime_now = r.elapsed.total_seconds()
#     #     customize_dict['restime_now'] = restime_now
#     #     self.assertEqual(200, r_json['resp_code'])
#     #     self.assertEqual('SUCCESS', r_json['resp_msg'])
#     #     self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_019_goldenLetter_retrospective(self):
#         """金点信追溯"""
#         payload = {
#             "goldenLetterId": g_d.get("goldenLetterId")
#         }
#         r = api_goldenLetter_retrospective(token_scf_enterprise, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_020_goldenLetter_getBusType(self):
#         """判断审批类型"""
#         payload = {
#             "id": g_d.get("id")
#         }
#         r = api_goldenLetter_getBusType(token_scf_enterprise, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_021_goldenLetter_goldenLetterOpenSeal(self):
#         """金点信开立平台方审核签章返回地址"""
#         payload = {
#             "auditStatus": 3,
#             "goldenLetterId": g_d.get("goldenLetterId")
#         }
#         r = api_goldenLetter_goldenLetterOpenSeal(token_scf_enterprise, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_022_goldenLetter_updateGoldenLetterAddress(self):
#         """签章后更新文件地址"""
#         payload = {
#             "list": [
#                 {
#                     "address": "",
#                     "goldenLetterCode": ""
#                 }
#             ]
#         }
#         r = api_goldenLetter_updateGoldenLetterAddress(token_scf_enterprise, payload)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
