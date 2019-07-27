#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 17:02
# @Author  : SmallStrong
# @Des     : 
# @File    : model.py
# @Software: PyCharm

import sys

reload(sys)

sys.setdefaultencoding('utf8')
sys.path.append('/home/small/api/')
from sqlalchemy import Column, BigInteger, Integer, String, SmallInteger, Float, DateTime, Index, MetaData, \
    Table, PickleType, Boolean, DECIMAL, Text
from sqlalchemy.dialects.mysql import MEDIUMTEXT, LONGTEXT, DOUBLE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    user_id = Column(BigInteger, nullable=False, primary_key=True, comment="用户id")
    nick_name = Column(String(20), nullable=False, default="", comment='昵称')
    sex = Column(String(1), nullable=False, default="1", comment='性别 0女 1男 默认男')


class Message(Base):
    __tablename__ = 'message'
    message_id = Column(BigInteger, nullable=False, primary_key=True, autoincrement=True, comment="朋友圈信息id")
    user_id = Column(BigInteger, nullable=False, index=True, comment="用户id")
    content = Column(String(50), nullable=False, default="", comment='标题')
    ctime = Column(Integer, nullable=False, comment='创建时间轴')
    image_list = Column(String(10000), nullable=False, default="[]", comment='图片列表')
