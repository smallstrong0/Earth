#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 16:10
# @Author  : SmallStrong
# @Des     : 
# @File    : list.py
# @Software: PyCharm

import core.check as check
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import wte_api.dap.random_list


def go():
    keys = {

    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        _list = wte_api.dap.random_list.get_random_list()
        dic['result_list'] = _list
    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
