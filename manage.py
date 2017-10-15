#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

apis = {
    'test'
}


@app.route('/api/<func>', methods=['GET', 'POST'])
def hello_world(func):
    exec 'import ' + func
    data = eval(func + '.go()')
    return data


if __name__ == '__main__':
    app.run(debug=True)
