#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import dao.user as dao_user
import pymongo


def set_user_info(params):
    result = dao_user.select({'user_id': params['user_id']}, ['wechat_id', 'user_id'], 1, [('port', pymongo.ASCENDING)])
    if result.count() > 0:
        return dao_user.update({'user_id': params['user_id']}, {'user_info': params['user_info']})
    else:
        return False
