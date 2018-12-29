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
import pdf_api.dap.search


def go():
    keys = {
        'key': None,
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        _list = pdf_api.dap.search.key2search(params['key'])
        dic['result_list'] = _list
    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
