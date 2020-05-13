#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/13 10:22 
# @Author : qingping.niu
# @File : http_auth.py 
# @Desc : postman鉴权实例

from flask import Flask,jsonify,request,abort,url_for,make_response
from flask_httpauth import HTTPBasicAuth

u'''基于flask的web service的实例代码'''
app=Flask(__name__)

u'''增加HTTPBasicAuth的权限验证机制'''
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username =='wuya':
        return 'admin'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error':'Unauthorized access'}),401)

datas=[{
    'userid':1,
    'username':'李四',
    'phone':'13645874859'
}]

@app.route('/hotel/username/',methods=['GET'])
@auth.login_required
def show():
    return jsonify({'datas':datas})

if __name__=='__main__':
    app.run(debug=True)

