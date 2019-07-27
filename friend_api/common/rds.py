#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 上午11:41
# @Author  : SmallStrong
# @Des     : 
# @File    : sqlalchemy_demo.py
# @Software: PyCharm


from sqlalchemy.orm import sessionmaker, scoped_session
import friend_api.common.error_const as error_const
import json
import datetime
import decimal
from sqlalchemy.ext.declarative import DeclarativeMeta

import friend_api.tools.config as config

from sqlalchemy import create_engine

echo = True
conn = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(config.RDS_MYSQL['USER'],
                                                            config.RDS_MYSQL['PASSWORD'],
                                                            config.RDS_MYSQL['HOST'],
                                                            config.RDS_MYSQL['PORT'],
                                                            config.RDS_MYSQL['DB_NAME'])
engine = create_engine(conn,
                       pool_recycle=1800,  # pool_recycle 半小时自动断开连接 以免被mysql超时断开
                       pool_pre_ping=True,  # 每次连接MySQL先简单ping
                       pool_size=10,  # 线程池线程数量
                       echo=echo)  # 是否打印sql过程
Session = scoped_session(sessionmaker(bind=engine))


class cli:
    def __init__(self):
        self.session = Session()

    def sql(self, func):
        def wrapper(*args, **kw):
            try:
                return_data = func(*args, **kw)
                if return_data and type(return_data) == tuple and len(return_data) == 2:
                    error = return_data[0]
                    if error:  # 出现业务逻辑背离情况 事务执行需要回滚
                        print("出现业务逻辑背离情况 事务执行需要回滚")
                        self.session.rollback()
                        return error, {}
                    else:
                        print("正常情况 提交事务")
                        self.session.commit()  # 正常情况 提交事务
                        data = json.loads(sqlalchemy_serialize(return_data[1]))  # 对象转数据
                        return None, data
                else:
                    print("没有什么要返回的 正常情况 提交事务")
                    self.session.commit()  # 没有什么要返回的 正常情况 提交事务
                    return None, {}
            except Exception as e:  # 代码异常 被try捕捉
                print("*" * 50)
                print(e)
                print("*" * 50)
                self.session.rollback()
                return error_const.BG_RDS_CODE_ERROR, {}
            finally:
                self.session.close()

        return wrapper


class AlchemyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:  # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    elif isinstance(data, decimal.Decimal):
                        fields[field] = str(data)
                    else:
                        print 111, type(data), isinstance(data, decimal.Decimal)
                        fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def sqlalchemy_serialize(data):
    return json.dumps(data, cls=AlchemyJsonEncoder)
