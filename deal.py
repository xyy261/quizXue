import requests
import string
from urllib.parse import quote
from model import Bank
from config import Config


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
        counter = response.count(option)
        print(f' ·{option}: {counter}')

    return True
    
   
def solve(session, question):
    '''返回值True数据库包含此记录，False则需要添加数据'''
    print(question.content)
    print('-'*20)
    bank = db_qeury(session, question.content)
    if bank is not None:
        print('Answer: %s'%bank.answer)
        return True
    search(question)
    return False
