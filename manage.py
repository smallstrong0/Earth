#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/yy_api/<func>', methods=['GET', 'POST'])
def go(func):
    exec 'import yy_api.fe.' + func
    data = eval('yy_api.fe.' + func + '.go()')
    return data


@app.route('/blog_api/<func>', methods=['GET', 'POST'])
def go(func):
    exec 'import blog_api.fe.' + func
    data = eval('yy_api.fe.' + func + '.go()')
    return data


if __name__ == '__main__':
    app.run()
