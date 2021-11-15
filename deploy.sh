#!/bin/bash

cd /www/wwwroot/te-cs && git pull && source te-cs_venv/bin/activate
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip3 install -r requirements.txt

# uwsgi --ini uwsgi.ini
kill 3354