#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@file: main.py
@author: kessil
@contact: https://github.com/kessil/
@time: 2019年06月02日 15:58:23
@desc: Life is short, you need Python
'''

from adble import pull_xml, tap_screen
from model import Base, engine, Session,Bank, db_add, db_qeury
import requests
import string
from urllib.parse import quote
from config import Config
import re

filename = Config.XML_URI
question = None
Base.metadata.create_all(engine)
session = Session()



def search(question):
    '''搜索引擎检索题目'''
    content = re.sub(r'[\(（]出题单位.*', "", question.content)
    url = quote('https://www.baidu.com/s?wd=' + content, safe=string.printable)
    headers = Config.HEADERS
    response = requests.get(url, headers=headers).text
    if question.item1: print('A. %s: %d'%(question.item1, response.count(question.item1)))
    if question.item2: print('B. %s: %d'%(question.item2, response.count(question.item2)))
    if question.item3: print('C. %s: %d'%(question.item3, response.count(question.item3)))
    if question.item4: print('D. %s: %d'%(question.item4, response.count(question.item4)))
    return question


def run(session, question, ch=''):
    pull_xml(filename)
    current = Bank.from_xml(filename)
    if question:
        # if current == question:
        #     print('输入“n”或“N”退出！')
        #     return question
        # elif ch and ch in 'ABCD':
        if ch and ch in 'ABCD':
            question.answer = ch
            db_add(session, question)
           
    question = current
    print('\n%s\n%s'%('-'*min(len(question.content)*2, 120), question.content))
    bank = db_qeury(session, content=question.content)
    if bank:
        # items = [x for x in (bank.item1, bank.item2, bank.item3, bank.item4) if x]
        # index = ord(bank.answer)-65
        # if index < len(items):
        #     items[index] = f'{items[index]} <--- [{bank.answer}]'
        # options = '\n'.join(items)
        # print(f'\n{options}')
        print(f"\n手机提交答案后可直接回车 正确答案:  {bank.answer}\n")
        return question
    return search(question) 

ch = ''

while True:    
    question = run(session, question, ch)
    print('%s\n请先在手机提交答案，根据提交结果输入答案！'%('-'*min(len(question.content)*2, 120)))
    ch = input('请输入：').upper()

    if 'N' == ch:
        break

