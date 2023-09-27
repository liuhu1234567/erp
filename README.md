<<<<<<< HEAD
# 项目介绍

## 简介

基本框架使用 unittest，结合 requests 实现接口自动化；

使用 BeautifulReport 生成报告

## 文件夹结构
```shell

```cmd
./
├── case_api
├── case_data
├── common
│   ├── BeautifulReport
│   ├── do_config.py
│   ├── do_email.py
│   ├── do_faker.py
│   ├── do_mysql.py
│   ├── do_robot.py
│   ├── get_token.py
│   ├── global_variable.py
│   ├── __init__.py
│   └── upload_report.py
├── config
│   ├── all_path.py
│   ├── config.json
│   └── __init__.py
├── files
├── performance
├── README.md
├── result
│   ├── log
│   └── report
└── run.py
```

case_api：接口用例文件夹

case_data：已弃用

common：
- BeautifulReport 用于生成报告
- do_config.py 读取配置文件
- do_faker.py 生成随机数据
- do_mysql.py 连接MySQL数据库
- get_token.py 获取运营平台、业务平台的token
- global_variable 项目中自定义的变量储存在这
- upload_report.py 上传报告

config：
- all_path 项目中用到的路径
- config.json 项目配置

files：项目中上传、下载的文件都放在这里

performance：暂不做使用

result：
- log 日志保存的目录
- report 报告目录

run.py 入口

# 使用说明

1. 先抓取一个接口，如 http://192.168.12.143:9900/api-node/aa/bb
2. 将 url 按照 / 进行分割，得到4部分
   - data1 = http://192.168.12.143:9900，不用管，我们在config.json文件中配置
   - data2 = api-node
   - data3 = aa
   - data4 = bb
3. 在case文件夹下，新建 ${data3}_${data4}.py 文件
   - 文件中定义一个 api_${data3}_${data4} 的函数，封装业务接口
   - 用例类以文件名命名，用大驼峰写法
   - 用例方法命名：test_${data3}_${data4}
   - 如果一个方法不够，后面的方法命名规则： test_${data3}_${data4}_后缀
   - 用例的数据写在py文件中
4. 用例中，
   - token从get_token文件中获取，实现整个工程只登录一次
   - 下一个接口需要用到的数据可以通过键值对，保存到global_variable.py中的customize_dict字典中，供自由使用

## 配置文件说明

配置文件位置：config/config.json

```json
{
    "all_host": {
        "test": "测试环境的host地址",
        "prod": "生产环境的host地址"
    },
    "restime": "允许接口响应的最大时间，超过这个时间，用例为失败",
    "env_now": "当前使用哪个环境，从all_host中选择",
    "report_name": "报告名",
    "account_yy": {
        "username": "运营平台账号",
        "password": "密码"
    },
    "account_yw": {
        "username": "业务平台账号",
        "password": "密码"
    },
    "upload_report": {
        "upload_MeterShpere": "是否上传到MeterShpere，true：上传；false：不上传",
        "upload_robot": "是否使用机器人发送报告结果，true：上传；false：不上传",
        "upload_email": "是否使用邮件发送报告结果，true：上传；false：不上传"
    }
}
```

## 运行
在 config/config.ini 中进行项目配置

运行 run.py 文件
=======
# erp
>>>>>>> 36c8c85631ff07f4ab5a224876ea2ce146e0b231
