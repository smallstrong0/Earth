#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils as c_tool
import requests
import dap.recharge
import tool.t_utils as t_tool
from lxml import etree
import random


def go():
    keys = {
        'user_id': None,
        'money': None,
        'openid': None,
    }
    error, params = check.simple_go(keys)

    dic = {
    }

    if error is None:
        data, out_trade_no = dap.recharge.get_data(params)
        dic['out_trade_no'] = out_trade_no
        r = requests.post(
            'https://api.mch.weixin.qq.com/pay/unifiedorder', data)
        xml = etree.fromstring(r.content)  # 进行XML解析
        prepay_id = xml.find("prepay_id").text
        dap.recharge.get_pay_sign(prepay_id, dic)

    if error is None:
        return c_tool.check_sort_serialize(data=dic)
    else:
        return c_tool.check_sort_serialize(msg=error)
