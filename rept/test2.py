#!/usr/bin/python
# coding:utf8
import sys,urllib,urllib2
reload(sys)
sys.setdefaultencoding('gb2312')

LOGIN_HOST = "http://select.ycit.cn"
HOME_HOST = "http://select.ycit.cn/Student/Sinfo.aspx"

data = {
    "__VIEWSTATE": "dDwyMTExNzQ2MDEzO3Q8O2w8aTwxPjs+O2w8dDw7bDxpPDE1Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+Oz4+Oz4+Oz45tyHQI4oknqPXFhWDRHsQIsywPA==" \
    , "txtUsername": "1410060846", "txtPassword": "1410060846", 'butLogin': ' 登 录 '
    }
data = urllib.urlencode(data)
request = urllib2.Request(LOGIN_HOST)
print
'''
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
response = opener.open(LOGIN_HOST,data,20)
result = response.read()
'''
#print str(result).encode('utf-8')

