#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:15
# @Author  : SmallStrong
# @Des     : 
# @File    : list.py
# @Software: PyCharm

"""
@api {POST} message/list 朋友圈列表
@apiName list
@apiGroup message
@apiVersion 1.0.0

@apiParam {int} user_id 用户id
@apiParam {int} [page] 第几页 默认为1
@apiParam {int} [page_size] 每页条数 默认为10

@apiSuccessExample 返回例子
{
    "code": 200,
    "data": [
        {
            "content": "你好啊 大强子0",
            "ctime": 1564189449,
            "image_list": [
                "https://smallstrong.wang/friend_image/test.png"
            ],
            "message_id": 1,
            "user_id": 10086
        },
        {
            "content": "你好啊 大强子1",
            "ctime": 1564189449,
            "image_list": [
                "https://smallstrong.wang/friend_image/test.png"
            ],
            "message_id": 2,
            "user_id": 10086
        },
        {
            "content": "你好啊 大强子2",
            "ctime": 1564189449,
            "image_list": [
                "https://smallstrong.wang/friend_image/test.png"
            ],
            "message_id": 3,
            "user_id": 10086
        },
        {
            "content": "你好啊 大强子3",
            "ctime": 1564189449,
            "image_list": [
                "https://smallstrong.wang/friend_image/test.png"
            ],
            "message_id": 4,
            "user_id": 10086
        },
        {
            "content": "你好啊 大强子4",
            "ctime": 1564189449,
            "image_list": [
                "https://smallstrong.wang/friend_image/test.png"
            ],
            "message_id": 5,
            "user_id": 10086
        }
    ],
    "message": "ok"
}
"""

import core.check as check
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import friend_api.dap.message as message


def go():
    keys = {
        'user_id': None,  # 用户id
        'page': 1,
        'page_size': 10,
    }
    error, params = check.simple_go(keys)

    message_list = []

    if error is None:
        error, message_list = message.get_list(params['user_id'], int(params['page']), int(params['page_size']))
        for m in message_list:
            m['image_list'] = c_tool.deserialize(m.get('image_list', '[]'))
    if error is None:
        return c_tool.check_sort_serialize(data=message_list)
    else:
        return c_tool.check_sort_serialize(msg=error)
