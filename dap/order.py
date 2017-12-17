#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import dao.order as dao_order
import dap.get_user_coin
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
    return False
    coin = params['coin']
    user_coin = dap.get_user_coin.get_coin(params)
    if user_coin >= coin:
        return True
    else:
        return False
