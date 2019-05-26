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
import re
import string
from time import sleep
import requests
from lxml import etree
from urllib.parse import quote

question = {}
def pull_xml(filename):
    if os.path.exists(filename):
        os.remove(filename)
    os.system('adb shell uiautomator dump /sdcard/ui.xml')
    os.system('adb pull /sdcard/ui.xml %s'%filename)
    

def tap_andriod(x, y):
    print('tap (%d, %d)'%(x, y))
    sleep(15)
    os.system('adb shell input tap %d %d'%(x, y))


def analysis_xml(filename):
    global question
    pull_xml(filename)
    xml = etree.parse(filename)
    root = xml.getroot()
    qeustion = root.xpath('//node[@class="android.webkit.WebView"]/node/node[@index="2"]/node/node[@index="1"]/node[@index="0"]')[0]
    # print(qeustion)
    content = qeustion.xpath('./node[@index="0"]/@content-desc')[0]
    print(content)
    childs = qeustion.xpath('./node[@index="1"]//node/node[@index="1"]')
    options = []
    for child in childs:
        # print(child.xpath('./@bounds')[0])
        bounds = [int(x) for x in re.findall(r'\d+', child.xpath('./@bounds')[0])]
        options.append({
            "desc": child.xpath('./@content-desc')[0],
            "pos": (int((bounds[0]+bounds[2])/2), int((bounds[1]+bounds[3])/2)),
            "count": 0
        })
    if question and question['content'] == content:
        return False
    question = {
        'content': content,
        'options': options
    }
    return True

def search_by_baidu():
    global question
    for o in question['options']:
        if "以上全是" == o['desc']:
            tap_andriod(o['pos'])
            return
    content = re.sub(r'（.*）', '', question['content'])
    print(content)
    url = quote('https://www.baidu.com/s?wd=' + content, safe = string.printable)
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    response = requests.get(url, headers=headers).text
    # print(response)
    for o in question['options']:
        o['count'] = response.count(o['desc'])
        
    order_options = sorted(question['options'], key=lambda x: x['count'], reverse=True)
    for o in order_options:
        print('%s\t%d'%(o['desc'], o['count']))

    tap_andriod(*order_options[0]['pos'])

if __name__ == "__main__":
    filename = './xmls/ui.xml'
    # search_by_baidu(analysis_xml(filename))
    while analysis_xml(filename):
        search_by_baidu()
        
