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
from quesion import Question
from model import Base, engine, Session,Bank
import requests
import string
from urllib.parse import quote
from config import Config

filename = Config.XML_URI
question = None
Base.metadata.create_all(engine)
session = Session()


def db_add(session, question, ch=''):
    op = " ".join([x.desc for x in question.options])
    bank = Bank(content=question.content, options=op, answer=ch.upper())
    session.add(bank)
    session.commit()

def db_qeury(session, content):
    '''第一步、数据库检索题目'''
    return session.query(Bank).filter_by(content=content).first()

def search(question):
    '''第二步、搜索引擎检索题目'''
    content, options = question.content, question.options
    url = quote('https://www.baidu.com/s?wd=' + content, safe=string.printable)
    headers = Config.HEADERS
    response = requests.get(url, headers=headers).text
    for option in options:
        option.counter = response.count(option.desc)
        print(f' ·{option.desc}:\t{option.counter}')
    return question


def run(session, question, ch=''):
    pull_xml(filename)
    current = Question.from_xml(filename)
    if question:
        if current == question:
            return question
        elif ch and ch in 'ABCD':
            print('Execute session.add')
            db_add(session, question, ch)
        else:
            pass            
    question = current
    print('%s\n%s'%(question.content, '-'*min(len(question.content)*2, 80)))
    bank = db_qeury(session, question.content)
    if bank:
        print(f"\n手机提交答案后可直接回车 Answer:  __{bank.answer}__\n")
        return question
    return search(question) 

ch = ''
while True:    
    question = run(session, question, ch)
    print('%s\n请先在手机提交答案，根据提交结果输入答案！（“N”退出）'%('-'*min(len(question.content)*2, 80)))
    ch = input('请输入：').upper()

    if 'N' == ch:
        break
    # if 65 <= ord(ch) <= len(question.options) + 65:
    #     index = ord(ch.upper()) - 65
    #     tap_screen(*question.options[index].pos)






    

    
    

        
