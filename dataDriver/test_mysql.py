#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 10:25 
# @Author : qingping.niu
# @File : test_mysql.py 
# @Desc : 操作mysql数据库

import pymysql

def connMySql():
    try:
        con = pymysql.connect(host='127.0.0.1',user='root',password='123456',db='mytest')
        return con
    except:
        raise Exception('连接mysql数据库失败')

def insertOne():
    '''插入一条数据'''
    con = connMySql()
    cur = con.cursor()
    sql = 'insert into t_user values(%s,%s,%s,%s)'
    params=(0,'weke','123456','1364859563')
    cur.execute(sql,params)
    con.commit()
    cur.close()
    con.close()


def insertMany():
    '''插入多条数据'''
    con = connMySql()
    cur = con.cursor()
    sql = 'insert into t_user values(%s,%s,%s,%s)'
    params=[(0,'weike','adb','14253698'),
            (0,'lisi','123456','14828469527')]
    cur.executemany(sql,params)
    con.commit()
    cur.close()
    con.close()

def get_one():
    '''查询单条数据'''
    try:
        con = connMySql()
    except:
        raise Exception('连接mysql数据库失败')
    else:
        cur = con.cursor()
        sql='select * from t_user where id=%s'
        params=(1007,)
        cur.execute(sql,params)
        print('查询的结果:',cur.fetchone())
    finally:
        cur.close()
        con.close()

def get_many():
    '''批量查询数据'''
    try:
        con = connMySql()
    except:
        raise Exception('连接mysql数据库失败')
    else:
        cur = con.cursor()
        sql='select * from t_user'
        cur.execute(sql)
        print('查询的结果:')
        for item in cur.fetchall():
            print(item)
    finally:
        cur.close()
        con.close()

class MySqlHelper(object):
    def conn(self):
        '''连接mysql数据库'''
        try:
            con = pymysql.connect(
                host='127.0.0.1',
                user='root',
                password='123456',
                db='mytest')
            return con
        except:
            raise Exception('连接mysql数据库失败')

    def get_one(self,sql,params):
        try:
            cur = self.conn().cursor()
            cur.execute(sql,params)
            return cur.fetchone()
        except:
            pass
        finally:
            cur.close()
            self.conn().close()

class CheckUserInfo(MySqlHelper):
    def __init__(self):
        self.__helper=MySqlHelper()

    def checkUser(self,sql,parmas):
        return self.get_one(sql,parmas)

def userInfo():
    try:
        username=input('请输入账号:\n')
        password=input('请输入密码:\n')
        sql='select * from t_user where name=%s and password=%s'
        params=(username,password)
        check = CheckUserInfo()
        result = check.checkUser(sql,params)
        if result is not None:
            nick = result[1]
            print('登录系统成功,您的账号为:{}'.format(nick))
        else:
            print('您的账号或者用户名错误,请检查')
    except:
        raise Exception('系统出错')


if __name__=='__main__':
    # insertOne()
    # insertMany()
    # get_one()
    # get_many()
    userInfo()