# _*_ coding :utf-8
#@Author : 'zoubq'
# @Time : 2021/4/29 9:47
# @Function :


class EmailConfig:
    def __init__(self,on_off,mail_host,mail_user,mail_pass,mail_port,sender,receiver,subject,content):
        self.on_off = on_off
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass =mail_pass
        self.mail_port = mail_port
        self.sender = sender
        self.recevier = receiver
        self.subject = subject
        self.content = content