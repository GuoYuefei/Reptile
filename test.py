#!/usr/bin/python
#! coding:utf8
import urllib
import urllib2
import sys
#专门用于提交表单信息，主要用于模拟登录
class VLogin:
    reload(sys)
    sys.setdefaultencoding("gb2312")
    #用于存放html结果，之后可以推出其他类型
    html = ''
    #初始化类
    def __init__(self,url1,url2,data):
        #data为表单信息，loginUrl为提交表单目的地，resultUrl为提交之后的表单
        self.loginUrl = url1
        self.resultUrl = url2
        self.data = data

    # 获取cookie
    @property
    def __get_jsessionid(self):
        url = self.loginUrl
        response = urllib.urlopen(url)
        sid = str(response.headers['Set-Cookie'])[11:-7]
        return sid

    def do(self):
        sid = self.__get_jsessionid
        post_url = self.resultUrl+';jsessionid=' + sid
        post_data = self.data
        post_data = urllib.urlencode(post_data)     #编码成可发送的数据
        post_headers = {
            'Cookie': sid,
        }

        request = urllib2.Request(post_url, post_data, post_headers)
        response = urllib2.urlopen(request)
        self.html = str(response.read())
        self.html = self.html.decode("gb2312")
        self.html = self.html.encode("utf8")
        print self.html


if __name__ == '__main__':

    vlogin = VLogin("http://222.188.0.102/loginAction.do"
                    ,"http://222.188.0.102/loginAction.do"
                     ,{'zjh': '1410060846','mm': '1410060846'})
    '''
    vlogin = VLogin("http://localhost:8080/Struts/form/hello.jsp",
                    "http://localhost:8080/Struts/hello.do",
                    {'name':'123','passwd':'qwewq'})
    '''
    vlogin.do()