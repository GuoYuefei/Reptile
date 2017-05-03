import urllib
import httplib
test_data = {'name':'aaaa','passwd':'bbbbb'}
test_data_urlencode = urllib.urlencode(test_data)
requrl = "http://localhost:8080/Struts/hello.do"
headerdata = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'18',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'localhost:8080',
'Origin':'http://localhost:8080',
'Referer':'http://localhost:8080/Struts/form/hello.jsp',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
conn = httplib.HTTPConnection("localhost")
conn.request(method="POST",url=requrl,body=test_data_urlencode,headers = headerdata)
response = conn.getresponse()
res= response.read()
print res