#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 17:43
# @Author  : SmallStrong
# @Des     : 
# @File    : p.py
# @Software: PyCharm
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
import tool.c_utils
import pdf_api.common._redis as redis_go

redis_cli = redis_go.cli()

PDF_URL = 'pdf_set'
PDF_DIC_URL = 'pdf_dic_set'


def go():
    redis_cli.delete(PDF_URL)
    redis_cli.delete(PDF_DIC_URL)
    dic_list = []
    fh = open('./bc.txt')
    for line in fh.readlines():
        dic = {
            'name': line.split("链接:")[0].strip(),
            'url': line.split("链接:")[1].split("密码:")[0].strip(),
            'pw': line.split("密码:")[1].strip(),
        }
        dic_list.append(dic)
        redis_cli.sadd(PDF_URL, dic['name'])
        redis_cli.hmset(PDF_DIC_URL, {dic['name']: dic['url'] + "|||" + dic['pw']})
    print(tool.c_utils.sort_serialize(dic_list))


if __name__ == '__main__':
    go()
