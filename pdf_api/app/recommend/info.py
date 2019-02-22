#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 14:07
# @Author  : SmallStrong
# @Des     : 
# @File    : info.py
# @Software: PyCharm

import core.check as check
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import pdf_api.dap.recommend


def go():
    keys = {
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        _list = pdf_api.dap.recommend.info()
        dic['result_list'] = _list
    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
