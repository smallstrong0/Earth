#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import dao.address as dao_address
import pymongo


def add_address(params):
    params['address_id'] = c_tool.guid()
    return dao_address.create(params)


def mod_address(params):
    return dao_address.update({'user_id': params['user_id'], 'address_id': params['address_id']},
                              params)


def remove_address(params):
    return dao_address.delete(params)


def get_address_list(params):
    return dao_address.select({'user_id': params['user_id']}, [], 10, [('port', pymongo.ASCENDING)])
