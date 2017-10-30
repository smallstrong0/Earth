#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

whale_apis = {

    'login',  # 用户相关
    'mod_user_info',
    'get_user_info',
    'add_coin',

    'list_order',  # 订单相关
    'commit_order',
    'pay_order',

    'add_address',  # 地址相关
    'list_address',
    'mod_address',
    'remove_address',
}


@app.route('/api/<func>', methods=['GET', 'POST'])
def go(func):
    exec 'import fe.' + func
    data = eval('fe.' + func + '.go()')
    return data


if __name__ == '__main__':
    app.run(debug=True)
