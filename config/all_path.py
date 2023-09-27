import os

project_path = os.path.dirname(os.path.dirname(__file__))
report_dir = os.path.join(project_path, 'result', 'report')
case_api_dir = os.path.join(project_path, 'case_api')


def get_report_path(file_name):
    """传入报告文件名，获取报告文件的绝对路径"""
    report_path = os.path.join(report_dir, file_name)
    return report_path


def get_log_path(file_name):
    """传入日志文件名，获取日志文件的绝对路径"""
    log_dir = os.path.join(project_path, 'result', 'log')
    log_path = os.path.join(log_dir, file_name)
    return log_path


def get_case_data_path(file_name):
    """获取用例数据文件的绝对路径"""
    case_data_dir = os.path.join(project_path, 'case_data')
    case_data_path = os.path.join(case_data_dir, file_name)
    return case_data_path


def get_file_path(file_name):
    """获取上传文件的绝对路径"""
    files_dir = os.path.join(project_path, 'files')
    file_path = os.path.join(files_dir, file_name)
    return file_path


def get_config_path(file_name):
    """获取配置文件的绝对路径"""
    config_path = os.path.join(project_path, 'config', file_name)
    return config_path
