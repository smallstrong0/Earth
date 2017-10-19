#! /usr/bin/env python
# -*- coding: utf-8 -*-

import core.check as check


def go():
    keys = {
        'ts': None,
    }
    error, params = check.go(keys)
    if error is None:
        pass
