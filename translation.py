import requests
import whois as whois
import json
from urllib import request,parse
import random
import logging






headerstr = '''User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1
Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50)
'''

def headers():
    header = headerstr.split('\n')
    length = len(header)
    return header[random.randint(0, length - 1)]

youdaoUrl = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
headers = {"User-Agent":headers(),
           "X-Requested-With":"XMLHttpRequest", # 可以处理Ajax
           "Accept":"application/json, text/javascript, */*; q=0.01",# 可以接收json数据
           }




def fanyi(key):
    formdata = {"i": key,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "1527148862626",
                "sign": "547b8ff87043e3eecbc2d5446238fb4a",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTIME",
                "typoResult": "false"
                }
    # 做urlencode
    data = bytes(parse.urlencode(formdata), encoding="utf-8")  # 由于post
    # 需要发送bytes类型的数据，所以这个地方需要转换成bytes
    req = request.Request(youdaoUrl, data, headers, method="POST")
    repsonse = request.urlopen(req)
    info = repsonse.read().decode("utf-8")  # bytes -> json str
    # {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":0,"translateResult":[[{"src":"hi","tgt":"嗨"}]]}
    # i=hi&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1527148862626&sign=547b8ff87043e3eecbc2d5446238fb4a&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTIME&typoResult=false
    jsonLoads = json.loads(info)
    print(jsonLoads['translateResult'][0][0]['tgt'])



def info(object, spacing=15):
    """
     Print methods and doc strings. Take module, class,
     dictionary, or string.
    """
    # 遍历一遍object对象，把里面的可以被调用的方法提取出来
    methodList = [method for method in dir(object)
                  if callable(getattr(object, method))]
    # if callable(getattr(object, method))



    # 把要提取出来的方法以更好看的,多行变单行
    processFunc = lambda s: " ".join(s.split())

    # 让左端打印的是方法名称，右端打印的是方法的doc名称
    return ('\n'.join(["%s %s" % (str(method.ljust(len(method) + spacing)),
                                  processFunc(str(getattr(object, method).__doc__)))
                       for method in methodList]))


# fanyyi('''Random number generator base class used by bound module functions. Used to instantiate instances of Random to get generators that don't share state. Class Random can also be subclassed if you want to use a different basic generator of your own devising: in that case, override the following methods: random(), seed(), getstate(), and setstate(). Optionally, implement a getrandbits() method so that randrange() can cover arbitrarily large ranges.''')


if __name__ == '__main__':
    doc = []
    wenben = info(requests.get)

    # wenben1 = json.loads(wenben)
    t = wenben.split('\n')
    for x in t:
        # print(x[0:19],sep=' ')
        # fanyi(x[19::])
        doc.append({x[0:19]:x[19::]})

    for y in doc:
        for n in y:
            print(n)
            fanyi(y.get(n))
            print('\n')
