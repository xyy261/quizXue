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
from deal import solve
from model import Base, engine, Session,Bank
from config import Config

Base.metadata.create_all(engine)
session = Session()
def db_add(session, question, ch=''):
    op = " ".join([x for x in question.options])
    bank = Bank(content=question.content, options=op, answer=ch.upper())
    session.add(bank)
    session.commit()

filename = Config.XML_URI
while True:
    pull_xml(filename)
    question = Question.from_xml(filename)
    if solve(session, question):
        continue

    ch = input('请输入答案回车继续……')
    if 'n' == ch or 'N' == ch:
        break

    if ch in 'abcdABCD':
        db_add(session, question, ch)
    

    
    

        
