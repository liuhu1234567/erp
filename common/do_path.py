import os

project_path = os.path.dirname(os.path.dirname(__file__))


def get_abspath(*args):
    """获取上传文件的绝对路径"""
    path = os.path.join(project_path, *args)
    return path

r = get_abspath()
print(r)