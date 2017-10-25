#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check
import tool.c_utils


def go():
    keys = {
        'ts': None,
        'nonce': None,
        'test': None,
    }
    error, params = check.go(keys)
    if error is None:
        return tool.c_utils.sort_serialize(params)
    else:
        return 'bad'
