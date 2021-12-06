#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import platform
import uuid
import re


# Show information
def showinfo(tip, info):
    print("{}:{}".format(tip, info))


# Computer mac address
def mac_address():
    mac_info = uuid.uuid1().hex[-12:].upper()
    mac_info = '-'.join([mac_info[i:i + 2] for i in range(0, 11, 2)])
    return mac_info


# Print information
def print_info(language="cn"):
    if language == "cn":
        showinfo("操作系统及版本信息", platform.platform())
        showinfo("获取系统版本号", platform.version())
        showinfo("获取系统名称", platform.system())
        showinfo("系统位数", platform.architecture())
        showinfo("计算机类型", platform.machine())
        showinfo("计算机名称", platform.node())
        showinfo('MAC地址:', mac_address())
        showinfo("处理器类型", platform.processor())
        showinfo("计算机相关信息", platform.uname())
        showinfo('编译信息:', platform.python_build())
        showinfo('版本信息:', platform.python_version())
    elif language == "en":
        showinfo("Operating system and version information", platform.platform())
        showinfo("Get system version number", platform.version())
        showinfo("Get system name", platform.system())
        showinfo("System bits", platform.architecture())
        showinfo("Computer type", platform.machine())
        showinfo("computer name", platform.node())
        showinfo("Mac address", mac_address())
        showinfo("Processor type", platform.processor())
        showinfo("Computer related information", platform.uname())
        showinfo("compile info", platform.python_build())
        showinfo("version info", platform.python_version())


# Get computer information
def computer_info():
    return {
        "platform": platform.platform(),
        "version": platform.version(),
        "system": platform.system(),
        "architecture": platform.architecture(),
        "machine": platform.machine(),
        "node": platform.node(),
        "mac_address": mac_address(),
        "processor": platform.processor(),
        "uname": platform.uname(),
        "python_build": platform.python_build(),
        "python_version": platform.python_version()
    }


# Get public network address
def public_network(url=None, area=None):
    links = ["https://myip.ipip.net/", "https://myip.la/"]
    url = url if url else (links[1] if area else links[0])
    res = requests.get(url)
    res.encoding = "utf8"
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res.content.decode(errors="ignore")).group(0)
    return {"ip": ip, "text": res.text}


if __name__ == "__main__":
    print(public_network())
