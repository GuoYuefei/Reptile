#!/usr/bin/python
#! coding:utf8
# 万恶的教务处，我要抓取你
#
import requests,sys,bs4
reload(sys)
sys.setdefaultencoding("utf-8")

s=requests.session()
data={"_VIEWSTATE":"dDwyMTExNzQ2MDEzO3Q8O2w8aTwxPjs+O2w8dDw7bDxpPDE1Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+Oz4+Oz4+Oz45tyHQI4oknqPXFhWDRHsQIsywPA==",\
    "txtUsername":"1410060846","txtPassword":"1410060846"}        #设置表单对应的字典信息

res1 = s.post("http://select.ycit.cn/Default.aspx",data)                         #post后获取网页信息
res2 = s.get("http://select.ycit.cn/Student/Sinfo.aspx",cookies=res1.cookies)

print res2.text

