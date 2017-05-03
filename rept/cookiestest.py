#!/usr/bin/python
# coding:utf8

import urllib2,urllib
import cookielib

# 声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
# 创建一个头信息，模拟游览器
post_headers = {         #+';PVT=1482306093768',
            'Accept': 'text/html, application/xhtml + xml, application/xml;q = 0.9, image / webp, * / *;q = 0.8',
            'Accept - Encoding': 'gzip, deflate, sdch',
            'Accept - Language': 'zh - CN, zh;q = 0.8',
            'Cache - Control': 'max - age = 0',
            'Connection': 'keep - alive',
            'Host': 'select.ycit.cn',
            'Referer': 'http: // select.ycit.cn /?',
            'Upgrade - Insecure - Requests': '1',
            'User - Agent': 'Mozilla / 5.0(X11;Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 55.0.2883.87 Safari / 537.36'
        }
# 要发送的数据
data = {'name': '1410060846', 'passwd': '1410060846'}
# 编码表单
data = urllib.urlencode(data)
# 此处创建一个请求实例
request = urllib2.Request('http://localhost:8080/Struts/form/hello.jsp',data=data)
# 打开这个请求实例
response = opener.open(request, timeout=20)
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value
print response.read()
