#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 08:15
# @Author  : SmallStrong
# @Des     :
# @File    : api_test.py
# @Software: PyCharm


import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
sys.path.append('/home/small/api/')
BASE_URL = u'https://pdf.smallstrong.wang/api/friend_api/app/'

import requests
import tool.c_utils as c_tool
from friend_api.dap.user import DEFAULT_USER_ID


def create_user():
    url = BASE_URL + 'user/create'
    p_data = {
        'nick_name': 'smallstrong',
        'sex': '1'
    }
    r = requests.post(url, json=p_data)
    r = c_tool.deserialize(r.text)
    print_func(r, sys._getframe().f_code.co_name)


def create_message():
    for i in xrange(100):
        url = BASE_URL + 'message/create'
        p_data = {
            'user_id': DEFAULT_USER_ID,
            'content': '你好啊 大强子{}'.format(i),
            'image_list': [u'https://smallstrong.wang/friend_image/test.png']
        }
        r = requests.post(url, json=p_data)
        r = c_tool.deserialize(r.text)
        print_func(r, sys._getframe().f_code.co_name)


def get_message_list():
    for i in xrange(1, 10):
        url = BASE_URL + 'message/list'
        p_data = {
            'user_id': DEFAULT_USER_ID,
            'page': i,
            'page_size': 5
        }
        r = requests.post(url, json=p_data)
        r = c_tool.deserialize(r.text)
        print_func(r, sys._getframe().f_code.co_name)


def print_func(result, method):
    if result.get('code', '') == 200:
        print('{} success !'.format(method))
        print c_tool.sort_serialize(result)
    else:
        print('{} failed !'.format(method))


if __name__ == '__main__':
    create_user()
    create_message()
    get_message_list()
