#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check


def go():
    keys = {
        'ts': None,
        'nonce': None,
        'test': None,
    }
    error, params = check.go(keys)
    if error is None:
        print params
        return 'intersting'
    else:
        return 'bad'
