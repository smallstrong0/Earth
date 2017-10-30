#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool


def go():
    keys = {
        'user_id': None,
        'nonce': None,
        'test': None,
    }
    error, params = check.go(keys)

    if error is None:
        print c_tool.check_sort_serialize(data=params)
        return c_tool.check_sort_serialize(data=params)
    else:
        print c_tool.check_sort_serialize(msg='error')
        return c_tool.check_sort_serialize(msg='error')
