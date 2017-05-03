#!/usr/bin/python
# coding:utf8
import sys,urllib,urllib2
reload(sys)
sys.setdefaultencoding('gb2312')

LOGIN_HOST = "http://222.188.0.102/loginAction.do"
HOME_HOST = "http://222.188.0.102/loginAction.do"

data = {'zjh': '1410060846', 'mm': '1410060846'}
data = urllib.urlencode(data)
request = urllib2.Request(LOGIN_HOST)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor)
response = opener.open(LOGIN_HOST,data,20)
result = response.read()

print str(result).encode('utf-8')

