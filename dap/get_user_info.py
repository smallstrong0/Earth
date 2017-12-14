#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import dao.user as dao_user
import pymongo


def get_info(params):
    result = dao_user.select({'user_id': params['user_id']}, [], 1, [('port', pymongo.ASCENDING)])
    if result.count() > 0:
        return result[0]
    else:
        return None
