#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tool.c_utils as c_tool
import tool.t_utils as t_tool
import pymongo
import key
import random
import yy_api.dao.user as dao_user

recharge = {
    '100': 10,
    '500': 550,
    '1000': 110,
    '2000': 230,
    '5000': 600,
}


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


def let_add_coin(params, total_fee):
    error = None
    if key.DEBUG:
        coin = recharge['{}'.format(int(params['money']) * 100)]
    else:
        coin = recharge['{}'.format(total_fee)]

    result = dao_user.select({'user_id': params['user_id']}, ['coin', 'user_id'], 1, [('port', pymongo.ASCENDING)])
    _coin = 0
    if result.count() > 0:
        _coin = result[0]['coin'] + coin
        b = dao_user.update({'user_id': params['user_id']}, {'coin': _coin})
        if not b:
            error = '添加失败'
    else:
        error = '找不到用户'

    return error, _coin
