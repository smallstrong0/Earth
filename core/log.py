#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import logging

"""
引用方式：
import core.log

log = core.log.Logger()


def go():
    log.debug('一个debug信息')
    log.info('一个info信息')
    log.warn('一个warning信息')
    log.error('一个error信息')
    log.critical('一个致命critical信息')
    
    
warn及以上级别的日志会被记录在 /home/small/whale/whale.log下，方便查错

续： uwsgi日志和这个logging日志想做功能方面的区分

"""


class Logger:
    def __init__(self):
        self.logger = logging.getLogger('')
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('%(asctime)s %(pathname)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(logging.INFO)

        self.logger.addHandler(sh)  # 设置文件日志

        fh = logging.FileHandler('/home/small/whale/whale.log')
        fh.setFormatter(fmt)
        fh.setLevel(logging.WARN)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
