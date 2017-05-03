#!/usr/bin/python
# ! coding:utf8
import urllib
import urllib2
import sys

# 专门用于提交表单信息，主要用于模拟登录
class VLogin:
    # 用于存放html结果，之后可以推出其他类型
    reload(sys)
    sys.setdefaultencoding('gb2312')
    html = ''

    # 初始化类
    def __init__(self, url1, url2, data):
        # data为表单信息，loginUrl为提交表单目的地，resultUrl为提交之后的表单
        self.loginUrl = url1
        self.resultUrl = url2
        self.data = data
        self.__get_jsessionid()

    # 获取cookie
    def __get_jsessionid(self):
        url = self.loginUrl
        response = urllib.urlopen(url)
        self.sid = str(response.headers['Set-Cookie'])[18:-7]
        print(response.headers['Set-Cookie'])
        """for k in response.headers:
            print k+'\t'+response.headers[k]
        print
        print response.getcode()
        print
        print response.info()
        print
        print response.geturl()
        """

    def do(self):
        post_url = self.loginUrl                #+ '?ASP.NET_SessionId=' + self.sid+'&PVT=1482306093768'
        post_data = self.data
        post_data = urllib.urlencode(post_data)  # 编码成可发送的数据
        post_headers = {
            'Cookie': 'JSESSIONID='+self.sid,#'ASP.NET_SessionId='+self.sid,         #+';PVT=1482306093768',
            'User - Agent': 'Mozilla / 5.0(X11;Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 55.0.2883.87 Safari / 537.36'
        }
        #创建要访问的request
        request = urllib2.Request(post_url, post_data,post_headers)
        #发送并接收
        response = urllib2.urlopen(request,timeout=20)
        self.html = str(response.read())
        self.html = self.html
        print(self.html)


if __name__ == '__main__':
    url1 = "http://select.ycit.cn/Default.aspx"
    url2 = "http://select.ycit.cn/Student/Sinfo.aspx"
    data = {
            "__VIEWSTATE": "dDwyMTExNzQ2MDEzO3Q8O2w8aTwxPjs+O2w8dDw7bDxpPDE1Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+Oz4+Oz4+Oz45tyHQI4oknqPXFhWDRHsQIsywPA=="
            ,"txtUsername": "1410060846", "txtPassword": "1410060846"
            , 'butLogin': ' 登 录 '
        }

    '''url1 = "http://localhost:8080/Struts/hello.do"
    url2 = 'http://localhost:8080/Struts/form/hello.jsp'

    data={'name' : '1234','passwd':'1234'}'''

    vLogin = VLogin(url2, url2, data)
    print(vLogin.sid)
    vLogin.do()