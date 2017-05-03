#!/usr/bin/python
#! coding:gb2312
#
from Reptile.rept.test import VLogin
import sys
reload(sys)
sys.setdefaultencoding("gb2312")
if __name__=="__main__":
    url1 = "http://select.ycit.cn"
    url2 = "http://select.ycit.cn/Student/Sinfo.aspx"
    data = {"__VIEWSTATE":"dDwyMTExNzQ2MDEzO3Q8O2w8aTwxPjs+O2w8dDw7bDxpPDE1Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+Oz4+Oz4+Oz45tyHQI4oknqPXFhWDRHsQIsywPA=="\
                ,"txtUsername": "1410060846","txtPassword": "1410060846",'butLogin':' 登 录 '.decode("gb2312")
            }
    headers = {
            'Accept': 'text/html, application/xhtml + xml, application/xml;q = 0.9, image / webp, * / *;q = 0.8',
            'Accept - Encoding':'gzip, deflate, sdch',
            'Accept - Language':'zh - CN, zh;q = 0.8',
            'Cache - Control':'max - age = 0',
            'Connection':'keep - alive',
            'Host':'select.ycit.cn',
            'Referer':'http: // select.ycit.cn /?',
            'Upgrade - Insecure - Requests':'1',
            'User - Agent':'Mozilla / 5.0(X11;Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 55.0.2883.87 Safari / 537.36'
                }
    vLogin = VLogin(url1,url2,data)
    vLogin.do()