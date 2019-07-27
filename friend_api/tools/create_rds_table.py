#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:17
# @Author  : SmallStrong
# @Des     : 
# @File    : create_rds_table.py
# @Software: PyCharm

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('/etc/fanfan/')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
sys.path.append('/home/small/api/')
import config

from sqlalchemy import create_engine
from friend_api.dao.model import Base

conn = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(config.RDS_MYSQL['USER'],
                                                            config.RDS_MYSQL['PASSWORD'],
                                                            config.RDS_MYSQL['HOST'],
                                                            config.RDS_MYSQL['PORT'],
                                                            config.RDS_MYSQL['DB_NAME'])

engine = create_engine(conn, encoding='utf-8')


def go():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    go()
