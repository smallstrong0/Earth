#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import pymongo
import key
import random


def get_pay_sign(prepay_id, dic):
    pay_sign = ''
    appId = key.appId
    timeStamp = t_tool.get_ts()
    nonceStr = random.randint(100000, 999999)
    package = 'prepay_id={}'.format(prepay_id)
    signType = 'MD5'

    _list = ['appId={}&'.format(appId), 'timeStamp={}&'.format(timeStamp), 'nonceStr={}&'.format(nonceStr),
             'package={}&'.format(package), 'signType={}&'.format(signType)]
    _list = sorted(_list)

    for i in _list:
        pay_sign = pay_sign + i
    pay_sign = pay_sign + 'key={}'.format(key.store_key)

    pay_sign = str(c_tool.md5(pay_sign)).upper()
    dic['timeStamp'] = timeStamp
    dic['nonceStr'] = nonceStr
    dic['paySign'] = pay_sign
    dic['package'] = 'prepay_id={}'.format(prepay_id)
    dic['signType'] = 'MD5'


def get_data(params):
    app_id = key.appId
    body = '有印充值中心'
    mch_id = key.mch_id
    nonce_str = random.randint(100000, 999999)
    notify_url = 'https://www.smallstrong.site'
    openid = params['openid']
    out_trade_no = "yy{}".format(t_tool.get_ts())
    spbill_create_ip = key.ip
    if key.DEBUG:
        total_fee = 1
    else:
        total_fee = int(params['money']) * 100
    sign = paysignjsapi(app_id, body, mch_id, nonce_str, notify_url, openid, out_trade_no,
                        spbill_create_ip, total_fee)

    formData = "<xml>"
    formData += "<appid>{}</appid>".format(app_id)
    formData += "<body>{}</body>".format(body)
    formData += "<mch_id>{}</mch_id>".format(mch_id)
    formData += "<nonce_str>{}</nonce_str>".format(nonce_str)
    formData += "<notify_url>{}</notify_url>".format(notify_url)
    formData += "<openid>{}</openid>".format(openid)
    formData += "<out_trade_no>{}</out_trade_no>".format(out_trade_no)
    formData += "<spbill_create_ip>{}</spbill_create_ip>".format(spbill_create_ip)
    formData += "<total_fee>{}</total_fee>".format(total_fee)
    formData += "<trade_type>JSAPI</trade_type>"
    formData += "<sign>{}</sign>".format(sign)
    formData += "</xml>"

    return formData


def paysignjsapi(app_id, body, mch_id, nonce_str, notify_url, openid, out_trade_no,
                 spbill_create_ip, total_fee):
    m_str = ''
    _list = ['appid={}&'.format(app_id), 'body={}&'.format(body), 'mch_id={}&'.format(mch_id),
             'nonce_str={}&'.format(nonce_str), 'notify_url={}&'.format(notify_url), 'openid={}&'.format(openid),
             'out_trade_no={}&'.format(out_trade_no), 'spbill_create_ip={}&'.format(spbill_create_ip),
             'total_fee={}&'.format(total_fee), 'trade_type={}&'.format('JSAPI')]
    _list = sorted(_list)

    for i in _list:
        m_str = m_str + i

    m_str = m_str + 'key={}'.format(key.store_key)
    return str(c_tool.md5(m_str)).upper()
