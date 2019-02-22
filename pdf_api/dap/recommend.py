#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 17:10
# @Author  : SmallStrong
# @Des     : 
# @File    : recommend.py
# @Software: PyCharm


TABS = ['前端', '后端', '移动端', '算法', '大数据']

INFO_LIST = [
    {
        "tab": "后端",
        "data_list": [
            {
                "book_name": "Python Web开发实战（董伟明）",
                "password": "sygf",
                "url": "https://pan.baidu.com/s/1kdt2EIYwROfKdQU-FhSW9A"
            },
            {
                "book_name": "redis设计与实现(第二版)",
                "password": "uwhv",
                "url": "https://pan.baidu.com/s/1eXmSAhntWE3Bm2qbOn3QAg"
            },
            {
                "book_name": "Redis深度历险",
                "password": "bpuy",
                "url": "https://pan.baidu.com/s/1zm-8BS_8KkUbLxks0pdXJw"
            },
            {
                "book_name": "MySQL技术内幕(InnoDB存储引擎)第2版",
                "password": "ahj9",
                "url": "https://pan.baidu.com/s/1U0v64UJyFqSiaVkRE4Gd4g"
            },
        ]
    }
]


def info():
    return INFO_LIST
