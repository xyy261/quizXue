#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: kessil
@license: LGPL
@contact: https://github.com/kessil?tab=repositories
@software: None
@file: NAME.py
@time: DATA TIME
@desc: NO_DESC
'''
import os
import subprocess
from config import Config
from time import sleep

def pull_xml(filename):
    if os.path.exists(filename):
        os.remove(filename)
    os.system('adb shell uiautomator dump /sdcard/ui.xml')
    os.system('adb pull /sdcard/ui.xml %s'%filename)

def tap_screen(x, y):
    # print('tap (%d, %d)'%(x, y))
    os.system('adb shell input tap %d %d'%(x, y))

if __name__ == "__main__":
    # os.system('adb shell getevent -p')
    # print(os.system('adb shell getevent -p'))
    filename = Config.XML_URI
