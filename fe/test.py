#! /usr/bin/env python
# -*- coding: utf-8 -*-

import lib.common.func as cn_func


def go():
    keys = {
        'ts': None,
    }

    params, error = cn_func.get_web_params(keys)
    return cn_func.check_sort_serialize(params)
