#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 23:19
# @Author  : SmallStrong
# @Des     : 
# @File    : create.py
# @Software: PyCharm

"""
@api {POST} message/create 发朋友圈
@apiName create
@apiGroup message
@apiVersion 1.0.0

@apiParam {int} user_id 用户id
@apiParam {String} content 标题
@apiParam {array} image_list 图片列表

@apiSuccessExample 返回例子
{
    "code": 200,
    "data": {},
    "message": "ok"
}
"""
import core.check as check
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import friend_api.dap.message as message


def go():
    keys = {
        'user_id': None,
        'content': None,
        'image_list': [],
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        error, dic = message.post_message(int(params['user_id']), str(params['content']),
                                          c_tool.serialize(params['image_list']), t_tool.get_ts())
    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
