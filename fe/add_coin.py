#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import requests
import dap.add_coin
import tool.t_utils as t_tool
from lxml import etree
import random


def go():
    keys = {
        'user_id': None,
        'money': None,
        'openid': None
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        data = dap.add_coin.get_data(params)
        r = requests.post(
            'https://api.mch.weixin.qq.com/pay/unifiedorder', data)
        print r.content

        xml = etree.fromstring(r.content)  # 进行XML解析
        prepay_id = xml.find("prepay_id").text  # 获得用户所输入的内容
        print prepay_id
        pay_sign = dap.add_coin.get_pay_sign(prepay_id)
        dic['timeStamp'] = t_tool.get_ts()
        dic['nonceStr'] = random.randint(100000, 999999)
        dic['package'] = 'prepay_id={}'.format(prepay_id)
        dic['signType'] = 'MD5'
        dic['paySign'] = pay_sign

    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
