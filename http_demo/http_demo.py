#!/usr/bin/sh python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 16:46 
# @Author : qingping.niu
# @File : http_demo.py 
# @Desc : http状态码

from flask import Flask,jsonify,request,abort,url_for,make_response
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

datas = [
    {
        'userid':1,
        'username':'李四',
        'phone':'1325478486'
    }
]

@app.route('/user/',methods=['GET'])
def get_user():
    return jsonify({'datas':datas})

@app.route('/user/',methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json:
        abort(400)

    data = {
        'userid':datas[-1]['userid']+1,
        'username':request.json['username'],
        'phone':request.json.get('phone','13287904597')
    }
    datas.append(data)
    return jsonify({'data':data},201)

if __name__ == '__main__':
    app.run(debug=True)
