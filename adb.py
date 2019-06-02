#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@file: adb.py
@author: kessil
@contact: https://github.com/kessil/
@time: 2019年06月02日 15:57:23
@desc: Life is short, you need Python
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

def connect_mumu():
    os.system('adb connect 127.0.0.1:7555')

if __name__ == "__main__":
    out = subprocess.Popen('adb shell uiautomator dump /sdcard/ui.xml', shell=True, stdout=subprocess.PIPE)
    out = subprocess.Popen('adb pull /sdcard/ui.xml', shell=True, stdout=None)

