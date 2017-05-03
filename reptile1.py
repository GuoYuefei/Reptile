#!/usr/bin/python
#! coding:utf8
# 一个小爬虫 我的第一个python爬虫诞生啦

import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
res = requests.get("http://www.sina.com.cn/")

res.encoding = 'utf-8'
f = file("/home/fly/Documents/res/xinlang","w+",1)
#f.Encoding = 'utf-8'
f.write(res.text)
f.flush()
f.close()
print(res.text)