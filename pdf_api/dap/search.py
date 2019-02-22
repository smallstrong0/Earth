#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 16:13
# @Author  : SmallStrong
# @Des     : 
# @File    : search.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import pdf_api.common._redis as redis_go
import tool.c_utils as c_tool

redis_cli = redis_go.cli()

PDF_URL = 'pdf_set'
PDF_DIC_URL = 'pdf_dic_set'


def key2search(key):
    d = redis_cli.hgetall(PDF_DIC_URL)
    s = redis_cli.smembers(PDF_URL)
    result_list = []
    for k in list(s):
        if str(key).upper() in str(k).upper():
            url_key_list = str(d[k]).split("|||")
            dic = {
                'book_name': k,
                'url': url_key_list[0],
                'password': url_key_list[1],
            }
            result_list.append(dic)
    return result_list


