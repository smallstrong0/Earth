#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 18:51
# @Author  : SmallStrong
# @Des     : 
# @File    : wx_check.py
# @Software: PyCharm


import core.check as check
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import hashlib

"""
{
    "CreateTime": "1548159945", 
    "Event": "subscribe", 
    "EventKey": "", 
    "FromUserName": "o0uhvuBRpTm2L19YT-6JYtq4fmqI", 
    "MsgType": "event", 
    "ToUserName": "gh_654d3c2e4eb3"
}
"""


def go():
    keys = {
        'signature': "",
        'timestamp': "",
        'nonce': "",
        'echostr': "",

    }

    error, params = check.simple_go(keys)

    print(params)
    print("hahah")

    signature = params['signature']
    timestamp = params['timestamp']
    nonce = params['nonce']
    echostr = params['echostr']
    token = "ea0cb648197411e9a3d100163e062a02"  # 自己设置的token

    _list = [token, timestamp, nonce]
    _list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, _list)
    hashcode = sha1.hexdigest()
    # sha1加密算法

    # 如果是来自微信的请求，则回复echostr
    if hashcode == signature:
        return echostr
    else:
        return ''
