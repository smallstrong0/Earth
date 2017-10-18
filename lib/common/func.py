#! /usr/bin/env python
# -*- coding: utf8 -*-

import time
import datetime
import json
import random
import hashlib
import math
import uuid
import HTMLParser
import calendar
import string
from Crypto.Cipher import DES, AES
from binascii import b2a_hex, a2b_hex
from flask import Flask, request

key = 'bda630k5-393d-0o2c-a907-312ea466'
mode = AES.MODE_CBC


def decode_html(s):
    return HTMLParser.HTMLParser().unescape(s)


def guid():
    return str(uuid.uuid1())


def hash(plain):
    return hashlib.sha1(plain).hexdigest()


def serialize(data):
    """
    序列化
    :param data:
    :return:
    """
    try:
        return json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    except Exception as e:
        return None


def deserialize(data):
    """
    反序列化
    :param data:
    :return:
    """
    try:
        return json.loads(data)
    except Exception as e:
        return None


def sort_serialize(data):
    """
    对数据字典进行排序
    :param data:
    :return:
    """
    try:
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    except Exception as e:
        # print e
        return None


def check_sort_serialize(data=None, msg=None):
    """
    data传一个字典过来, msg传错误信息。两者不兼容！！！，有data不传msg,有msg不传data
    :param data:
    :param msg:
    :return:
    """
    if msg is not None and len(msg) > 0:  # 说明有错误
        return sort_serialize({"data": {}, "code": -1, "message": msg})
    elif msg is None and data is not None:
        return sort_serialize({"data": data, "code": 200, "message": "ok"})


def get_web_params(keys):
    """
    参数校验
    :param keys:
    :return:
    """
    params = {}
    params_list = eval(request.values.items().__str__())
    for param in params_list:
        params[param[0]] = param[1]

    for key in keys:
        if key not in params:
            if keys[key] is None:
                return {}, (-1, 'param <{}> is missing'.format(key))
            else:
                params[key] = keys[key]
    if params.has_key('user_id'):
        try:
            long(params['user_id'])
        except Exception as e:
            return {}, (-1, 'invalid user_id = {}'.format(params['user_id']))

    return params, None


def decrypt(text):
    """
    AES 解密
    :param text:
    :return:
    """
    cryptor = AES.new(key, mode, b'0000000000000000')
    plain_text = cryptor.decrypt(a2b_hex(text))
    return plain_text.rstrip('\0')


def encrypt(text):
    """
    AES加密
    :param text:
    :return:
    """
    cryptor = AES.new(key, mode, b'0000000000000000')
    # 这里密钥key 长度必须为16（AES-128）,
    # 24（AES-192）,或者32 （AES-256）Bytes 长度
    # 目前AES-128 足够目前使用
    length = 16
    count = len(text)
    if count < length:
        add = (length - count)
        # \0 backspace
        text = text + ('\0' * add)
    elif count > length:
        add = (length - (count % length))
        text = text + ('\0' * add)
    ciphertext = cryptor.encrypt(text)
    # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    # 所以这里统一把加密后的字符串转化为16进制字符串
    return b2a_hex(ciphertext)


if __name__ == '__main__':
    print encrypt('aaa0cdsncoudncioandsicojnasiopcjnasiopcjnioasjncioadsncioadsncionasdiocnasiocnasioncsioancsiao0000')
    print decrypt(
        encrypt('aaa0cdsncoudncioandsicojnasiopcjnasiopcjnioasjncioadsncioadsncionasdiocnasiocnasioncsioancsiao0000'))
