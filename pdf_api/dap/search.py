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

pic_name = [
    "Ansible自动化运维与技术与最佳实践",
    "JavaScript高级程序设计（第3版）",
    "Vim实用技巧",
    "Netty实战",
    "Tensorflow 实战Google深度学习框架",
    "TCP-IP详解(卷一、二、三)",
    "Shell脚本学习指南  完整版",
    "Shell脚本学习指南  完整版",
    "设计模式-java-刘伟",
    "selenium2 python自动化测试",
    "Redis深度历险",
    "Redis开发与运维",
    "redis设计与实现(第二版)",
    "Python基础教程（第3版）",
    "Python Web开发实战（董伟明）",
    "Linux高性能服务器编程",
    "Practical Common Lisp",
    "MySQL性能调优与架构设计+",
    "Java虚拟机（第二版)",
    "Linux 命令行 - v1.0",
    "Lisp - The Little Schemer (4th Endition)",
    "Go 源码剖析（书签版）",
    "Go语言实战",
    "Java 8实战",
    "go语言圣经（中文版）",
    "App研发录：架构设计、Crash分析和竞品技术分析(包建强)",
    "C++ Primer 中文第四版(非扫描)",
    "CPU自制入门",
    "Effective Java 第二版 中文版",
    "Elasticsearch 权威指南（中文版）",
    "Go 语言详解（书签版）",
    "图解密码技术(日)结城浩(著)  人民邮电出版社 2014-12-01 PDF电子书带详细书签目录 完整版",
    "深入理解Android WiFi NFC和GPS卷（邓凡平）",
    "深入理解Android卷1（邓凡平）",
    "统计学习方法（李航）",
    "深入理解Android 卷2（邓凡平）",
    "编程之美",
    "剑指Offer",
    "垃圾回收的算法与实现",
    "流畅的Python",
    "深入解析Go内核实现",
    "鸟哥的Linux私房菜-基础学习篇(第四版)",
    "鸟哥的Linux私房菜基础班（第四版）",
    "鸟哥的Linux私房菜服务器架设篇(第三版)",
    "2018年美团点评技术年货（合）",
    "《Go语言编程》高清完整版电子书",
    "《HTTP权威指南》迷你书",
    "《图解TCP IP(第5版)》",
    "MySQL技术内幕(InnoDB存储引擎)第2版",
    "Linux高性能服务器编程"
]


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
                'img': "http://small-1254418121.file.myqcloud.com/pdf/{}.jpg".format(k) if k in pic_name else ""
            }
            result_list.append(dic)
    return result_list
