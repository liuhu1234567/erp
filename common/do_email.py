import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.global_variable import customize_dict

sender = "autotest@dianliantech.com"
password = "autotest@2022"
receivers = "xiangziliang@dianliantech.com"


def send_email(file_url):
    """发送邮件"""
    testName = customize_dict['resultData']['testName']
    testAll = customize_dict['resultData']['testAll']
    testPass = customize_dict['resultData']['testPass']
    testFail = customize_dict['resultData']['testFail']
    beginTime = customize_dict['resultData']['beginTime']
    totalTime = customize_dict['resultData']['totalTime']
    testSkip = customize_dict['resultData']['testSkip']
    testError = customize_dict['resultData']['testError']

    msg = MIMEMultipart()

    msg["Subject"] = testName
    msg["From"] = sender
    msg["To"] = receivers

    content = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>自动化测试报告</title>
</head>

<body>
    <table style="text-align: left; border-collapse: collapse; width: 700px; border: 0.5px dashed black; font-size: 30px;">
        <caption>{testName}</caption>
        <tr>
            <td style="border: 0.5px dashed black;">总用例数</td>
            <td style="border: 0.5px dashed black;">{testAll}</td>
        </tr>
        <tr style="color: #00dd00;">
            <td style="border: 0.5px dashed black;">通过用例数</td>
            <td style="border: 0.5px dashed black;">{testPass}</td>
        </tr>
        <tr style="color: red;">
            <td style="border: 0.5px dashed black;">失败用例数</td>
            <td style="border: 0.5px dashed black;">{testFail}</td>
        </tr>
        <tr style="color: #dddd00;">
            <td style="border: 0.5px dashed black;">跳过用例数</td>
            <td style="border: 0.5px dashed black;">{testSkip}</td>
        </tr>
        <tr style="color: red;">
            <td style="border: 0.5px dashed black;">报错用例数</td>
            <td style="border: 0.5px dashed black;">{testError}</td>
        </tr>
        <tr>
            <td style="border: 0.5px dashed black;">开始运行时间</td>
            <td style="border: 0.5px dashed black;">{beginTime}</td>
        </tr>
        <tr>
            <td style="border: 0.5px dashed black;">运行时间</td>
            <td style="border: 0.5px dashed black;">{totalTime}</td>
        </tr>
        <tr>
            <td style="border: 0.5px dashed black;">详细报告</td>
            <td style="border: 0.5px dashed black;"><a href="{file_url}" target="_blank">点击查看</a></td>
        </tr>
    </table>
</body>

</html>"""
    html = MIMEText(content, "html", "utf-8")
    msg.attach(html)

    smtpserver = "mail.sunwoda.com"
    smtp = smtplib.SMTP()
    try:
        smtp.connect(smtpserver)
        smtp.login(sender, password)
        smtp.sendmail(sender, receivers, msg.as_string())
        print('邮件发送成功')
    except Exception as e:
        print(f'邮件发送发生错误：{e}')
    finally:
        smtp.quit()
