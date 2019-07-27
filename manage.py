#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 08:54
# @Author  : SmallStrong
# @Des     :
# @File    : flask
# @Software: PyCharm

from flask import Flask
from flask import make_response

app = Flask(__name__)


@app.route('/api/yy_api/<func>', methods=['GET', 'POST'])
def yy_go(func):
    exec 'import yy_api.fe.' + func
    data = eval('yy_api.fe.' + func + '.go()')
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/api/blog_api/<func>', methods=['GET', 'POST'])
def blog_go(func):
    exec 'import blog_api.fe.' + func
    data = eval('blog_api.fe.' + func + '.go()')
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/api/wte_api/app/<module>/<func>', methods=['GET', 'POST'])
def wte_go(module, func):
    exec 'import wte_api.app.{}.{}'.format(module, func)
    data = eval('wte_api.app.{}.{}.go()'.format(module, func))
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/api/pdf_api/app/<module>/<func>', methods=['GET', 'POST'])
def pdf_go(module, func):
    exec 'import pdf_api.app.{}.{}'.format(module, func)
    data = eval('pdf_api.app.{}.{}.go()'.format(module, func))
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/api/friend_api/app/<module>/<func>', methods=['GET', 'POST'])
def friend_go(module, func):
    exec 'import friend_api.app.{}.{}'.format(module, func)
    data = eval('friend_api.app.{}.{}.go()'.format(module, func))
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run()
