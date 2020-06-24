# coding=utf-8
# -*- coding: utf-8 -*-

'''
Created on May 23, 2019
进行http请求
# json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
@author: canace
'''
import requests
import json
import logging as logger


class RunMain():

    def send_post(self, url, data):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data).json()  # 因为这里要封装post方法，所以这里的url和data值不能写死
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)  
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, data=data)
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        logger.info(data)
        if method == 'post':
            result = self.send_post(url, data)
            logger.info(str(result.encode('utf-8')))
        elif method == 'get':
            result = self.send_get(url, data)
            logger.info(str(result).encode('utf-8'))
        else:
            print("method值错误！！！")
            logger.sendLogger("method值错误！！！")
        return result


if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    logger.info('1')
    result = RunMain().run_main('post', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=')
#     result = RunMain().run_main('get', 'http://www.baidu.com')
    print result
