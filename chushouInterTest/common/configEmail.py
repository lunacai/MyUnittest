# coding=utf-8
'''
Created on May 23, 2019

@author: canace
'''
import os
import readConfig
import getpathInfo
from common.Log import logger
from email.mime.text import MIMEText
import smtplib

read_conf = readConfig.ReadConfig()
mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')  # 获取测试报告路径
# 使用smpt发送邮件
msg_server = read_conf.get_email('msg_server')
password = read_conf.get_email('password')
msg_from = read_conf.get_email('msg_from')
msg_to = read_conf.get_email('msg_to')
msg_subject = read_conf.get_email('msg_subject')
logger = logger


class send_email():

    def smtp_send(self):
        content = """
                    执行测试中......
                    执行已完成!!
                    生成报告中......
                    报告已生成......
                    报告已邮件发送！！
                    """ + str(mail_path)
        message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message['From'] = "{}".format(msg_from)
        message['To'] = msg_to
        message['Subject'] = msg_subject
        print message

        try:
            smtpObj = smtplib.SMTP_SSL(msg_server, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(msg_from, password)  # 登录验证
            smtpObj.sendmail(msg_from, msg_to, message.as_string())  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)


if __name__ == '__main__':  # 运营此文件来验证写的send_email是否正确
    send_email().smtp_send()
    print("send email ok!!!!!!!!!!")
