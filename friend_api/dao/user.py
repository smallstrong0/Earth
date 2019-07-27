#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:21
# @Author  : SmallStrong
# @Des     : 
# @File    : user.py
# @Software: PyCharm


from model import User
from friend_api.common.rds import cli
import friend_api.common.error_const as error_const

mysql = cli()


@mysql.sql
def add(user):
    mysql.session.add(user)
