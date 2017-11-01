#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import dao.login as dao_login
import pymongo


def get_wx_user_id(openid):
    result = dao_login.select({'wechat_id': openid}, ['wechat_id', 'user_id'], 1, [('port', pymongo.ASCENDING)])
    if result.count() > 0:
        return result[0]['user_id']
    else:
        data = dao_login.create(
            {'wechat_id': openid, 'user_id': c_tool.guid(), 'ctime': t_tool.get_ts(), 'mtime': t_tool.get_ts()})
        if data:
            return data['user_id']
        else:
            return None
