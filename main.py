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
from andriod_handle import pull_xml, tap_screen
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
    '''第二步、搜索引擎检索题目'''
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
        if current == question:
            print('输入“n”或“N”退出！')
            return question
        elif ch and ch in 'ABCD':
            question.answer = ch
            db_add(session, question)
           
    question = current
    print('\n%s\n%s'%(question.content, '-'*min(len(question.content)*2, 80)))
    bank = db_qeury(session, content=question.content)
    if bank:
        print(f"\n手机提交答案后可直接回车 Answer:  -{bank.answer}-\n")
        return question
    return search(question) 

ch = ''

while True:    
    question = run(session, question, ch)
    print('%s\n请先在手机提交答案，根据提交结果输入答案！'%('-'*min(len(question.content)*2, 80)))
    ch = input('请输入：').upper()

    if 'N' == ch:
        break







    

    
    

        
