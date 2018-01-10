#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 上午8:53
# @Author  : SmallStrong
# @Des     : 用builtwith模块去分析一个网站使用了哪些技术栈
# @File    : bw.py
# @Software: PyCharm
import builtwith
import tool.c_utils

SITE = 'https://www.smallstrong.site'


def web_built_with():
    print tool.c_utils.sort_serialize(builtwith.parse(SITE))


if __name__ == '__main__':
    web_built_with()
