#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:21
# @Author  : SmallStrong
# @Des     : 
# @File    : message.py
# @Software: PyCharm


from model import Message
from friend_api.common.rds import cli
import friend_api.common.error_const as error_const

mysql = cli()


@mysql.sql
def add_message(message):
    mysql.session.add(message)


@mysql.sql
def get_message_list(user_id, page, page_size):
    start = (page - 1) * page_size
    end = page_size * page
    message_list = mysql.session.query(Message).filter(Message.user_id == user_id)[start:end]
    return None, message_list
