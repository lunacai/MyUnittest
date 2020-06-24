# coding:utf-8
""" 
数据库管理类    user库
"""
from datetime import datetime
import requests
from DBUtils.PooledDB import PooledDB
import MySQLdb
import BusinessBases as bb
import ipConfigs as ip


# 自定义的配置文件，主要包含DB的一些基本配置
# 数据库实例化类
class DbManager():

    def __init__(self):
        if ip.IP == ip.IP174:
            self._pool = PooledDB(MySQLdb, ip.maxconnections, host='192.168.16.176', user='dev', passwd='dev',
                                  db='jellyfish_user', port=3308, charset="utf8")  # 5为连接池里的最少连接数#
        else:
            self._pool = PooledDB(MySQLdb, ip.maxconnections, host=ip.host, user='script_user',
                                  passwd='user_4_script', db='jellyfish_user', port=ip.port, charset="utf8")  # 5为连接池里的最少连接数#

    def getConn(self):
        return self._pool.connection()


_dbManager = DbManager()


def getConn():
    """ 获取数据库连接 """
    return _dbManager.getConn()


def executeAndGetId(sql, param=None):
    """ 执行插入语句并获取自增id """
    conn = getConn()
    cursor = conn.cursor()
    if param == None:
        cursor.execute(sql)
    else:
        cursor.execute(sql, param)
    id = cursor.lastrowid
    cursor.close()
    conn.close()
    return id


def updateExecute(sql):
    """ 修改数据 """
    conn = getConn()
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def deleteExecute(sql):
    """ 删除数据 """
    conn = getConn()
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def execute(sql, param=None):
    """ 执行sql语句 """
    conn = getConn()
    cursor = conn.cursor()
    if param == None:
        rowcount = cursor.execute(sql)
    else:
        rowcount = cursor.execute(sql, param)
    cursor.close()
    conn.close()
    return rowcount


def queryOne(sql):
    """ 获取一条信息 """
    conn = getConn()
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    rowcount = cursor.execute(sql)
    if rowcount > 0:
        res = cursor.fetchone()
    else:
        res = None
    cursor.close()
    conn.close()
    return res


def queryAll(sql):
    """ 获取所有信息 """
    conn = getConn()
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    rowcount = cursor.execute(sql)
    if rowcount > 0:
        res = cursor.fetchall()
    else:
        res = None
    cursor.close()
    conn.close()
    return res


def resultRow(n, sql):
    if n == 1:
        row = queryOne(sql)
        return row
    elif n == 2:
        rows = queryAll(sql)
        return rows


def getChuShouUserProfileUid(uid, n=1):  # 根据用户uid查询
    sql = 'SELECT * FROM `chushou_user_profile` where uid=' + str(uid)
    return resultRow(n, sql)


def getToken(uid):  # 通过uid获取token
    try:
        u_id = str(uid)
        i = uid % 256
        row = queryOne('SELECT token FROM token_info_' + str(i) + 
                       '  WHERE uid = ' + u_id + ' order by created_time desc')
        if row == None:
            token = loginInfo(uid)  # 没有token则通过登录获取
        else:
            conn = getConn()
            cursor = conn.cursor()
            t = str(row["token"])
            cursor.execute('SELECT HEX(' + t + ')')
            rows1 = cursor.fetchone()
            for row1 in rows1:
                token = row1
            cursor.execute('SELECT HEX(' + u_id + ')')
            rows = cursor.fetchone()
            for row in rows:
                token = token + 'g' + row
                break
        return token.encode("utf-8")
    except MySQLdb.Error, e:
        log.info("Mysql Error %d: %s" % (e.args[0], e.args[1]))


def loginInfo(uid):
    row = getChuShouUserProfileUid(uid)
    if row != None:
        username = row["username"]
        password = row["password"]
        t = bb.getTimeStamp()  # 获取时间戳
        _appkey = bb.getAppkey()
        value = {'password': password, 'username': username,
                 '_appkey': _appkey, '_t': t, '_appVersion': "4.9"}
        value = dict(value, **bb.CommonParameter(_appkey, "post"))
        _sign = bb.getSignValue(value)
        value.update({'_sign': _sign})  # 将_sign加入到values中
        values = ""
        for v in value:
            values = values + "&" + v + "=" + str(value[v])
        url = bb.IP + '/api/chushou-login.htm?' + values
        print url
        f = urllib.urlopen(url)
        s = f.read()
        if s != None and s != '':
            print s
            bbs = json.loads(s)
            if bbs["code"] == 0:
                return bbs["data"]["token"]
        return ""
    else:
        return ""
