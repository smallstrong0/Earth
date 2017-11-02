#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import dao.user as dao_user
import pymongo


def get_wx_user_id(openid):
    result = dao_user.select({'wechat_id': openid}, ['wechat_id', 'user_id'], 1, [('port', pymongo.ASCENDING)])
    if result.count() > 0:
        return result[0]['user_id']
    else:
        data = dao_user.create(
            {'wechat_id': openid, 'user_id': c_tool.guid()})
        if data:
            return data['user_id']
        else:
            return None
