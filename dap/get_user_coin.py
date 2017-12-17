#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import dao.user as dao_user
import pymongo


def get_coin(params):
    result = dao_user.select({'user_id': params['user_id']}, ['coin'], 1, [('port', pymongo.ASCENDING)])

    if result.count() > 0:
        print list(result)[0]
        return list(result)[0]['coin']
    else:
        return 0
