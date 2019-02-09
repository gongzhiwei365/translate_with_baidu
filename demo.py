# /usr/bin/env python
# coding=utf8

import httplib2
import hashlib
import urllib
import random
import json

appid = '20181126000239659'  # 你的appid
secretKey = 'ICIDfkcUrlxUmxYipw74'  # 你的密钥

myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
q = input("请输入要翻译的英文:")
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)  # 随机数

sign = appid + q + str(salt) + secretKey
m1 = hashlib.md5()
m1.update(sign.encode('utf-8'))
sign = m1.hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
    q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

try:
    # 获取HTTP对象
    httpClient = httplib2.Http()
    # 发出同步请求，并获取内容
    response, content = httpClient.request(myurl)
    if (None != response):
        print("2333,你得到了翻译结果咯。")
    result=json.loads(content)["trans_result"][0]
    print(result['src']+" 翻译成中文为: "+result['dst'])
except Exception as e:
    print
    e
