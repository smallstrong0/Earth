#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import yy_api.dao.user as dao_user
import pymongo


def get_wx_user_id_and_coin(openid):
    result = dao_user.select({'wechat_id': openid}, ['wechat_id', 'user_id', 'coin'], 1, [('port', pymongo.ASCENDING)])
    if result.count() > 0:
        return result[0]
    else:
        data = dao_user.create(
            {'wechat_id': openid, 'user_id': c_tool.guid(), 'coin': 0})
        if data:
            return data
        else:
            return None
