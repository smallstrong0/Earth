#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
接收数据处理：
1.对接受到的数据进行AES解密，得到json文本
2.解密玩后反序列化json文本，得到字典
3.进行必要参数的校验
4.有需要检验用户的进行token校验
5.进行参数有效性校验，包括时效性和正确性
6.对字典进行，非必要却没传的字段进行补充并返回数据
"""

from Crypto.Cipher import DES, AES
from binascii import b2a_hex, a2b_hex
from flask import Flask, request
import tool.t_utils as t_tool
import tool.c_utils as c_tool

key = 'bda630k5-393d-0o2c-a907-312ea466'
mode = AES.MODE_CBC


def go(keys):
    error = None
    params = {}
    params_list = eval(request.values.items().__str__())
    if len(params_list) == 1:
        text = params_list[0][1]
        try:
            json_string = decrypt(text)
        except Exception as e:
            error = -1, '解密失败'
            print e
        if error is None:
            try:
                params = c_tool.deserialize(json_string)
            except Exception as e:
                error = -2, '反序列化失败'
                print e
        if error is None:
            params, error = get_web_params(keys, params)
        if error is None:
            if params.has_key('user_id'):
                token = check_token(params.get('user_id'))
                if token is not None:
                    if params.get('token', '') == token:
                        error = verify_sig(keys=params)
                    else:
                        error = -4, 'token 被篡改'
                else:
                    error = -3, 'token 过期 或者 找不到token'
            else:
                error = verify_sig(keys=params)
        if error is None:
            for k in keys:
                if k not in params:
                    params[k] = keys[k]

    return error, params


def check_token(user_id):
    """
    校验token，服务端控制一个token的生命周期，一个token超过这个时期就重新设置并返回token校验失败
    :param user_id:
    :return:
    """
    token = ''
    return token


def get_web_params(keys, params):
    """
    参数校验
    :param keys:
    :param params:
    :return:
    """
    for k in keys:
        if k not in params:
            if keys[k] is None:
                return {}, (-1, 'param <{}> is missing'.format(k))
    if params.has_key('user_id'):
        try:
            long(params['user_id'])
        except Exception as e:
            return {}, (-1, 'invalid user_id = {}'.format(params['user_id']))

    return params, None


def verify_sig(keys):
    """
    三分钟时效性校验 与 参数校验
    :param keys:
    :param token:
    :return:
    """
    error = None
    if keys.has_key('sig'):
        sig = keys.get('sig', '')
        sig_life = 300
        if (t_tool.get_ts() + sig_life) < long(keys.get('ts')):
            error = -5, '接口时效性失败'
        del keys['sig']
        if sig == c_tool.hash(c_tool.serialize(keys)):
            keys['sig'] = sig
        else:
            error = -6, '签名失败'
    return error


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
    print decrypt('xsaxasx')
