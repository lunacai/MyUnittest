# coding=utf-8
'''
Created on May 23, 2019

@author: canace
'''
import sys
sys.path.append('..')
import json
import requests
import chushouPub.BusinessBases as bb
import chushouPub.ipConfigs as ip
import chushouPub.poolDbJellyfishUser as bsUser
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urlparse
import readExcel
import common.Log
log = common.Log.logger
  
url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')

 
@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
 
    def setParameters(self, case_name, hostip, path, values, method, assertDate):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.hostip = str(hostip)
        self.path = str(path)
        self.values = str(values)
        self.method = str(method)
        self.assertDate = int(assertDate)
  
    def description(self):
        """
        test report description
        :return:
        """
        self.case_name
  
    def setUp(self):
        """
        :return:
        """
        print(self.case_name + "测试开始前准备")
  
    def test01case(self):
        userprofie = self.values
        path = self.path
        hostip = self.hostip
        allvalues = json.loads(userprofie)
        for key in allvalues.keys():
            if key == 'token':
                uid = int(allvalues[key])
                token = bsUser.getToken(uid)
                allvalues[key] = token
        print allvalues
        self.checkResult(hostip, path, allvalues)
  
    def tearDown(self):
        print("测试结束，输出log完结\n\n")
  
    def checkResult(self, hostip, path, values):  # 断言
        """
        check test result
        :return:
        """
        if hostip == "chat":
            url = ip.chatRoomIP
        elif hostip == "vchushou":
            url = ip.IP + path + '.htm'
        t = bb.getTimeStamp()  # 获取时间戳
        _appkey = bb.getAppkey()
        _appVersion = ip.version
        values.update({'_appkey':_appkey, '_t':t, '_appVersion':_appVersion, '_appSource':'100' })
        _sign = bb.getSignValue(values)
        values.update({'_sign':_sign})  # 将_sign加入到values中
        log.info(url)
        log.info(values)
        f = requests.post(url, data=values)
        log.info(f.text.encode('utf-8'))
        bbs = f.json()
        assert str(bbs['code']) == str(self.assertDate), str(bbs['code']) + '==' + str(self.assertDate)


if __name__ == '__main__':
    unittest.main()
    
