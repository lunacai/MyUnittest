# coding=utf-8
import ipConfigs as ip 
import requests
import hashlib
from random import choice

CSAndroid = "CSAndroid"  # , "安卓客户端"),
CSIos = "CSIos"  # , "苹果客户端"),


def getTimeStamp():  # 获取当前时间戳
    url = ip.IP + '/api/timestamp/get.htm'
    s = requests.get(url, headers={'Connection': 'close'})
    t = s.text
    return t


def getAppkey():
    _appkey = choice([CSAndroid, CSIos])
    return _appkey


def getSignValue(value):  # 获得签名
    src = 'HAL$#%^RTYDFGdktsf_)(*^%$'
    valueSort = sorted(value.iteritems(), key=lambda d: d[0], reverse=False)
    for vs in valueSort:
        src = src + "&" + str(vs[0]) + "=" + str(vs[1])
    _sign = get_md5_value(src)
    return _sign


def get_md5_value(src):  # MD5签名
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
