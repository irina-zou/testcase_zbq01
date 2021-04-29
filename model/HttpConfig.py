# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/28 21:45
# @Function :


class HttpCinfig(object):
    def __init__(self, baseurl, port, timeout):
        self.baseurl = baseurl
        self.port = port
        self.timeout = timeout
