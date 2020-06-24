# coding=utf-8
'''
Created on May 23, 2019

@author: canace
'''
import os
import ConfigParser as configparser
import getpathInfo  # 引入我们自己的写的获取路径的类

path = getpathInfo.get_Path()  # 调用实例化，还记得这个类返回的路径为 /Users/kascend/eclipse-workspace/chushouInterTest
config_path = os.path.join(path, 'config.ini')  # 这句话是在path路径下再加一级，最后变成 /Users/kascend/eclipse-workspace/chushouInterTest/config.ini
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path)


class ReadConfig():  # 读取对应配置的内容

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
    print 'HTTP中的baseurl值为：', ReadConfig().get_http('baseurl')
    print 'EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off') 

