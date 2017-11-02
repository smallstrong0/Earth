#! /usr/bin/env python
# -*- coding: utf-8 -*-
import core.mongo as db_core
import tool.c_utils
import tool.t_utils

collection = db_core.DbUtils().db.address

"""
字段规则
ctime
mtime
address_id 地址唯一id
user_id 用户ID全局唯一 UUID生成
name 收货人姓名
phone 电话
qq qq号
we_chat 微信号
address 地址
place 具体门牌号
"""


def create(dic={}):
    dic['ctime'] = tool.t_utils.get_ts()
    dic['mtime'] = tool.t_utils.get_ts()
    code = collection.insert(dic)
    if code:
        print dic
        return dic
    else:
        return None


def update(old={}, new={}):
    return True if collection.update(old, {'$set': new}) else False


def select(where={}, field=[], limits=3, ordering=[]):
    return collection.find(where, field).limit(limits).sort(ordering)


def delete(field={}):
    return True if collection.remove(field) else False
