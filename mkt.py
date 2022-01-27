#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os


def web_mkt():
    cmd = 'dir'
    # os.system(cmd)
    res = os.popen(cmd)
    opt_str = res.read()
    print(opt_str)


if __name__ == '__main__':
    web_mkt()
