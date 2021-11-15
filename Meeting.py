#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from utils.SystemTool import print_info
import webbrowser
import schedule
import datetime
import logging
import time
import uuid

logging.basicConfig(filename='logger.log', level=logging.INFO)
LOG = logging.getLogger(__name__)

base_url = "https://advantest.webex.com/meet"
user_list = [
    {
        "id": 1,
        "name": "vincent.chu",
        "status": True,
        "rule": "",
        "date": "",
        "url": ""
    },
    {
        "id": 2,
        "name": "cheney.cao",
        "status": True,
        "rule": "",
        "date": "",
        "url": ""
    },
    {
        "id": 3,
        "name": "jesse.guo",
        "status": True,
        "rule": "",
        "date": "",
        "url": ""
    }
]


# Open browser
def web_browser(parm):
    webbrowser.open(parm["url"])
    LOG.info("Web browser %s" % parm["url"])


# Construction params
def structure_params():
    new_list = []
    for item in user_list:
        try:
            item["key"] = str(uuid.uuid4())
            item["date"] = str(datetime.datetime.now())
            item["url"] = item["url"] if item["url"] else base_url + "/" + item["name"]
            new_list.append(item) if item["status"] else print(item['name'])
        except Exception as e:
            LOG.error("Structure params: %s" % e)

    return new_list


# Start meeting
def start_meeting():
    user_data = structure_params()
    for item in user_data:
        try:
            if item["name"] == "vincent.chu":
                schedule.every().day.at("10:18").do(web_browser, url=item["url"])
            elif item["name"] == "jesse.guo":
                schedule.every().tuesday.at("12:58").do(web_browser, url=item["url"])
            elif item["name"] == "cheney.cao":
                schedule.every().tuesday.at("15:58").do(web_browser, url=item["url"])
            else:
                print('No more task...')
        except Exception as e:
            LOG.error("Start the meeting fail %s" % e)

    while True:
        schedule.run_pending()
        time.sleep(1)


# Test meeting
def test_meeting():
    user_data = structure_params()
    for item in user_data:
        try:
            if item["name"] == "vincent.chu":
                schedule.every(3).minutes.do(web_browser, parm=item)
            elif item["name"] == "jesse.guo":
                schedule.every(2).minutes.do(web_browser, parm=item)
            elif item["name"] == "cheney.cao":
                schedule.every(1).minutes.do(web_browser, parm=item)
            else:
                print('No more task...')
        except Exception as e:
            LOG.error("Start the meeting fail %s" % e)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    print_info()
    start_meeting()
