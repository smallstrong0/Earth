#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

whale_apis = {
    'test'
}


@app.route('/api/<func>', methods=['GET', 'POST'])
def go(func):
    exec 'import fe.' + func
    data = eval('fe.' + func + '.go()')
    return data


if __name__ == '__main__':
    app.run(debug=True)

