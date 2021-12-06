#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import uuid


class User:
    a = 'hh'
    b = 'bb'

    def __init__(self, uid, name):
        self.id = uid
        self.name = name


uname = {
    'id': uuid.uuid4(),
    'name': 'jerry'
}

if __name__ == '__main__':
    uc = User(uuid.uuid4(), 'jerry')
    for _ in dir(uc):
        # print(hasattr(uc, _))
        print(getattr(uc, _))

    # print(uc.__dict__)
    # print(uname.get('desc'))
