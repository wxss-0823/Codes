#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 16:11
# @Author  : wxss
# @File    : 2.smtp_email.py

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


sender = '2198993328@qq.com'    # 发件人邮箱
pw = 'qoffjutxwrqkebde'         # 授权码
receiver = '2890344780@qq.com'  # 收件人邮箱


def sendEmail():
    ret = True
    try:
        # 创建一个多级内容的实例
        multipart_msg = MIMEMultipart()
        # 这些信息不会显示在正文中，需要在完整文件中查看
        # 将具有字段名和值的标头添加到消息中。字段会被添加到消息的现有字段的末尾。
        multipart_msg['From'] = f"Wxss <{sender}>"  # 注意 qq 要求的文件头格式
        multipart_msg['To'] = f"Lxsy <{receiver}>"
        multipart_msg['Subject'] = Header('Python SMTP 邮件测试：2024/2/2', 'utf-8')

        # text 内容
        txt_msg = MIMEText('这是一封测试邮件', 'plain', 'utf-8')

        # 邮件正文内容
        multipart_msg.attach(txt_msg)

        # 构造附件 1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(str(open('test.txt', 'rb').read()), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="HelloWorld.txt"'

        # 添加邮件附件内容
        multipart_msg.attach(att1)

        # 创建一个 HTML 类型的文本内容，并添加图片
        html_txt_msg = """
        <head>
            <script>
                function move()
                {
                    var obj = document.getElementById("pic1");
                    var deltax, deltay;
                    deltax = (obj.offsetLeft + 154) % window.innerWidth
                    deltay = (obj.offsetTop + 154) % window.innerHeight
                    obj.style.left = deltax + 'px';
                    obj.style.top = deltay + 'px';
                }
            </script>
        </head>
        <body>
            <p>点击头像即可跳转至个人主页<p>
            <p style="position:absolute" id="pic1" onmousemove="move()">
                <a href="https://www.bilibili.com">
                    <img src="cid:avatar" width="70px">
                </a>
            </p>
        </body>
        """
        # 创建 Message 对象
        html_msg = MIMEText(html_txt_msg, 'html', 'utf-8')

        # 添加 HTML 内容
        multipart_msg.attach(html_msg)

        # 指定图片为当前目录
        pic_fp = open('avatar.jpg', 'rb')
        html_txt_msg_image = MIMEImage(pic_fp.read())
        pic_fp.close()

        # 定义图片 ID，在 HTML 文本中引用
        html_txt_msg_image.add_header('Content-ID', '<avatar>')
        # 添加图片内容
        multipart_msg.attach(html_txt_msg_image)

        # 邮箱的 SMTP 服务器
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 服务器登录
        server.login(sender, pw)
        # 发送邮件
        server.sendmail(sender, receiver, multipart_msg.as_string())
        # 关闭链接
        server.quit()
    except Exception as e:
        ret = False
        print(e)

    return ret


result = sendEmail()
if result:
    print("邮件发送成功")
else:
    print("邮件发送失败")
