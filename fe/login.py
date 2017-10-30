#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import requests


def go():
    keys = {
        'code': None,

    }
    error, params = check.simple_go(keys)

    dic = {
        'openid': '',
        'session_key': '',
        'user_id': ''
    }

    if error is None:
        r = requests.get(
            'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
                'wxe91e789389d690e9', '841d4c6f2089bce65cde91fa4d09fd52', params['code']))
        dic['open_id'] = r.json()['open']
        dic['session_key'] = r.json()['session_key']

    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
