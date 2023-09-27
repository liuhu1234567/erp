from config.all_path import get_config_path
import json
from string import Template
import time


def read_config():
    """读取config.json文件"""
    with open(get_config_path('config.json'), 'r', encoding='utf-8') as config_f:
        config = json.load(config_f)
    return config


start_time = time.strftime('%Y%m%d_%H-%M-%S')
_config = read_config()
restime = _config['restime']
env_now = _config['env_now']
environment = _config['environment']
test_type = _config['test_type']
report_name = Template(_config['report_name']).safe_substitute(start_time=start_time)
skyworth_partnership = _config['skyworth_partnership']
skyworth_erp = _config['skyworth_erp']
upload_MeterShpere = _config['upload_report']['upload_MeterShpere']
upload_robot = _config['upload_report']['upload_robot']
upload_email = _config['upload_report']['upload_email']
host_partnership = _config['all_host']['test_partnership']
host_erp = _config['all_host']['test_erp']
