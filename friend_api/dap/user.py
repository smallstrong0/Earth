#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:21
# @Author  : SmallStrong
# @Des     : 
# @File    : user.py
# @Software: PyCharm
import friend_api.dao.user
from friend_api.dao.model import User
import tool.c_utils as c_tool

DEFAULT_USER_ID = 10086


def add_user(nick_name='', sex='1'):
    user = User()
    user.nick_name = nick_name
    user.sex = sex
    user.user_id = DEFAULT_USER_ID  # 默认创建一个用户
    return friend_api.dao.user.add(user)
