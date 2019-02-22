#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 17:14
# @Author  : SmallStrong
# @Des     : 
# @File    : qiniu_tool.py
# @Software: PyCharm

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from qiniu import build_batch_stat, Auth, BucketManager
import c_utils
from key import QINIU

import pdf_api.common._redis as redis_go

redis_cli = redis_go.cli()
PDF_URL = 'pdf_set'
PDF_DIC_URL = 'pdf_dic_set'


def go():
    result_url_dic = {}
    result_name_list = []
    base_url = u'http://pkdsmwim0.bkt.clouddn.com/'
    q = Auth(QINIU['AK'], QINIU['SK'])
    bucket = BucketManager(q)
    bucket_name = 'small'
    # 前缀
    prefix = ''
    # 列举条目
    limit = 1000
    # 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
    delimiter = '.'
    # 标记
    marker = None
    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
    for data in c_utils.deserialize(info.text_body)['commonPrefixes']:
        result_url_dic[data + 'pdf'] = base_url + data + 'pdf'
        result_name_list.append(data + 'pdf')
    for s in result_name_list:
        code = redis_cli.sadd(PDF_URL, s)
        print(code)
        if not code:
            print(s)
    redis_cli.hmset(PDF_DIC_URL, result_url_dic)

    print c_utils.sort_serialize(result_url_dic)
    print c_utils.sort_serialize(result_name_list)

    print(len(result_name_list))


if __name__ == '__main__':
    go()
