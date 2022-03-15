#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask

from common.BaseClass import Student

app = Flask(__name__)


@app.route('/')
def home_index():
    BQ = Student('jerry', 18)
    return BQ.get_user_info()


if __name__ == '__main__':
    app.run()
