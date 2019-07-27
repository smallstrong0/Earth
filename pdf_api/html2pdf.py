#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 10:47
# @Author  : SmallStrong
# @Des     : 
# @File    : html2pdf.py
# @Software: PyCharm
import pdfkit
import os

LOCAL_IMG_PATH = './files'


def deal_pic():
    path = os.getcwd() + "/{}".format(LOCAL_IMG_PATH)
    _list, dic = write_name(path)
    return _list, dic


def write_name(path):
    _list = []
    dic = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            if name == '.DS_Store':
                pass
            else:
                index = int(name[0:2])
                _list.append(index)
                dic[index] = name
    return _list, dic


def sort_serialize(data):
    """
    对字典进行排序 记录打印的地方
    :param data:
    :return:
    """

    import json

    try:
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    except Exception as e:
        # print e
        return None


def html2pdf(result):
    pdfkit.from_file(result, 'o.pdf')
    pass


def go():
    _list, dic = deal_pic()
    print(sort_serialize(_list))
    print(sort_serialize(dic))
    result = []
    for i in dic:
        result.append('./files/{}'.format(dic[i]))

    print(sort_serialize(result))
    html2pdf(result)


if __name__ == '__main__':
    go()
