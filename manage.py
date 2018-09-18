#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 08:54
# @Author  : SmallStrong
# @Des     :
# @File    : flask
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)


@app.route('/api/yy_api/<func>', methods=['GET', 'POST'])
def yy_go(func):
    exec 'import yy_api.fe.' + func
    data = eval('yy_api.fe.' + func + '.go()')
    return data


@app.route('/api/blog_api/<func>', methods=['GET', 'POST'])
def blog_go(func):
    exec 'import blog_api.fe.' + func
    data = eval('blog_api.fe.' + func + '.go()')
    return data


if __name__ == '__main__':
    app.run()
