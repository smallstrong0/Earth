#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import yy_api.dao.order as dao_order
import yy_api.dap.get_user_coin
import yy_api.dao.user as dao_user
import pymongo


def add_order(params):
    return dao_order.create(params)


def mod_order(params):
    return dao_order.update({'user_id': params['user_id'], 'address_id': params['address_id']},
                            params)


def remove_order(params):
    return dao_order.delete(params)


def get_order_list(params):
    return dao_order.select({'user_id': params['user_id']})


def check_order(params):
    coin = params['coin']
    user_coin = dap.get_user_coin.get_coin(params)
    if int(user_coin) - int(coin) >= 0:
        _coin = int(user_coin) - int(coin)
        dao_user.update({'user_id': params['user_id']}, {'coin': _coin})
        return True
    else:
        return False
