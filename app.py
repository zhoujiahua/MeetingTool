#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask

from common.BaseClass import Student
from urllib import request

app = Flask(__name__)


def check_guacamole_domain(url=None):
    result = False
    try:
        if not url:
            return result

        with request.urlopen(str(url)) as file:
            result = True if file.status == 200 and file.reason == 'OK' else False

    except Exception as e:
        print('Check VNC domain fail %s' % e)

    finally:
        print(result)


@app.route('/')
def home_index():
    BQ = Student('jerry', 18)
    return BQ.get_user_info()


if __name__ == '__main__':
    logoUrl = 'https://2llgxjm.com/upload/f/logo%E5%89%AF%E6%9C%AC.png'
    check_guacamole_domain()
    app.run()
