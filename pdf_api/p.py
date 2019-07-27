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

import tool
import pdf_api.common._redis as redis_go

redis_cli = redis_go.cli()

PDF_URL = 'pdf_set'
PDF_DIC_URL = 'pdf_dic_set'


def sort_serialize(data):
    """
    对数据字典进行排序
    :param data:
    :return:
    """
    try:
        import json
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    except Exception as e:
        return None


def go():
    # redis_cli.delete(PDF_URL)
    # redis_cli.delete(PDF_DIC_URL)
    dic_list = []
    fh = open('./other.txt')
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


def other_go():
    dic_name = redis_cli.hgetall("PDF_KILLER")
    dic_bd = redis_cli.hgetall("PDF_BD")

    result = []
    f = open('other.txt', 'a')
    for i in dic_bd:
        if i in dic_name:
            pu = str(dic_bd[i]).split("||")
            if len(pu) == 2:
                p = pu[0]
                u = pu[1]
                if dic_name[i] and p and u:
                    result.append(
                        {
                            'name': str(dic_name[i]).replace(".pdf", ""),
                            'url': u,
                            'password': p,
                        }
                    )
                    s = '{} 链接:{}  密码:{}'.format(str(dic_name[i]).replace(".pdf", ""), u, p)
                    f.write(s)
                    f.write('\n')
    print(sort_serialize(result))
    print(len(result))


if __name__ == '__main__':
    # other_go()
    # go()

    fh = open('./bc.txt')
    _list = []
    for line in fh.readlines():
        _list.append(line.split("链接:")[0].strip())
    print sort_serialize(_list)

