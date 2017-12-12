#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import pymongo
import key
import random


def get_data(params):
    app_id = key.appId
    mch_id = key.mch_id
    out_trade_no = params['out_trade_no']
    nonce_str = random.randint(100000, 999999)
    sign = paysignjsapi(app_id, mch_id, nonce_str, out_trade_no)

    formData = "<xml>"
    formData += "<appid>{}</appid>".format(app_id)
    formData += "<mch_id>{}</mch_id>".format(mch_id)
    formData += "<nonce_str>{}</nonce_str>".format(nonce_str)
    formData += "<out_trade_no>{}</out_trade_no>".format(out_trade_no)
    formData += "<sign>{}</sign>".format(sign)
    formData += "</xml>"

    return formData


def paysignjsapi(app_id, mch_id, nonce_str, out_trade_no):
    m_str = ''
    _list = ['appid={}&'.format(app_id), 'mch_id={}&'.format(mch_id),
             'nonce_str={}&'.format(nonce_str),
             'out_trade_no={}&'.format(out_trade_no)]
    _list = sorted(_list)

    for i in _list:
        m_str = m_str + i

    m_str = m_str + 'key={}'.format(key.store_key)
    return str(c_tool.md5(m_str)).upper()
