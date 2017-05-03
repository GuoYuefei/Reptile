#!/usr/bin/python
# "_VIEWSTATE":"dDwyMTExNzQ2MDEzO3Q8O2w8aTwxPjs+O2w8dDw7bDxpPDE1Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+Oz4+Oz4+Oz45tyHQI4oknqPXFhWDRHsQIsywPA==",\
import requests,  bs4, re,urllib,urllib2,sys
import json
reload(sys)
sys.setdefaultencoding('gbk')


LOGIN_HOST = "http://222.188.0.102/loginAction.do"
HOME_HOST = "http://222.188.0.102/loginAction.do"
s = requests.session()


data = {'zjh'.decode('utf-8'): '1410060846'.encode(), 'mm': '1410060846'.encode()}
res1 = s.post(LOGIN_HOST, data=data)
cookie = res1.cookies
print cookie
jid = str(cookie)[38:-22]
print jid
headers = {
'Connection':'keep-alive',
'cookies' : jid+';',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
res2 = s.get(HOME_HOST,cookies=res1.cookies,headers=headers)
print res2.text
