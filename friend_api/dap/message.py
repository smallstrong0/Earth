#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:21
# @Author  : SmallStrong
# @Des     : 
# @File    : message.py
# @Software: PyCharm

import friend_api.dao.message
from friend_api.dao.model import Message


def post_message(user_id, content, image_list, ctime):
    message = Message()
    message.user_id = user_id
    message.content = content
    message.image_list = image_list
    message.ctime = ctime
    return friend_api.dao.message.add_message(message)


def get_list(user_id, page, page_size):
    return friend_api.dao.message.get_message_list(user_id, page, page_size)
