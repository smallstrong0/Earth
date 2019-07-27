#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:15
# @Author  : SmallStrong
# @Des     : 
# @File    : create.py
# @Software: PyCharm

"""
@api {POST} user/create 用户创建（默认创建一个id为10086的用户）
@apiName create
@apiGroup user
@apiVersion 1.0.0

@apiParam {String} nick_name 昵称
@apiParam {String} sex # 性别 (传 1 男 传 0 女)

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
import friend_api.dap.user as user


def go():
    keys = {
        'nick_name': None,  # 昵称
        'sex': None,  # 性别 (传 1 男 传 0 女)
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        error, dic = user.add_user(params['nick_name'], params['sex'])
    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
