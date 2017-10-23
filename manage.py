#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, abort, render_template_string

app = Flask(__name__)

whale_apis = {
    'test'
}


@app.route('/api/<func>', methods=['GET', 'POST'])
def go(func):
    # if func not in whale_apis:
    #     return abort(401)
    # else:
    #     exec 'import fe.' + func
    #     data = eval('fe.' + func + '.go()')
    #     return data
    exec 'import fe.' + func
    data = eval('fe.' + func + '.go()')
    return data


# @app.errorhandler(401)
# def page_unauthorized(error):
#     return render_template_string('<h1>{{ error_info }}</h1>', error_info=error), 401


if __name__ == '__main__':
    app.run(debug=True)
