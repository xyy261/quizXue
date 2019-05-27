# 导入:
from sqlalchemy import Column,Integer, String, Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config
import json

# 创建对象的基类:
Base = declarative_base()

# 定义Bank对象:
class Bank(Base):
    # 表的名字:
    __tablename__ = 'Bank'

    # 表的结构:
    id = Column(Integer,primary_key=True)
    content = Column(Text, unique=True)
    options = Column(Text)
    answer = Column(String(128))

    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'options': self.options,
            'answer': self.answer
        }

    def __repr__(self):
        temp = "\n+ ".join(self.options.split(' '))
        return f'\n{self.id}. {self.content}\t **{self.answer.upper()}**\n\n\n+ {temp}\n'

# 初始化数据库连接:
engine = create_engine(Config.DATABASE_URI)

# 创建DBSession类型:
Session = sessionmaker(bind=engine)

def db_add(session, data):
    session.add(data)
    session.commit()

def db_update(session, data):
    pass


if __name__ == "__main__":
    # 创建数据表
    Base.metadata.create_all(engine)
    session = Session()

    # del_rec = session.query(Bank).filter_by(id=284).first()
    # session.add(Bank(id=8,content=del_rec.content, options=del_rec.options, answer=del_rec.answer))
    # session.delete(del_rec)
    # session.commit()

    one = session.query(Bank).all()
    print(f'题库规模： {len(one)} 题')
    with open('data-prod.md', 'w', encoding='utf-8') as fp:
        fp.write(f'# 学习强国题库：{len(one)} 题')
        for o in one:
            if o.answer:
                fp.write(str(o))
            # print(o)
    # print(f'\n题库规模： {len(one)} 题')
    # two = session.query(Bank).filter_by(answer='').all()
    # print(len(two))
    # for t in two:
    #     print(t)
    #     ch = input("修正答案:")
    #     t.answer = ch.upper()
    # session.commit()
    # content="在我国，ABO血型系统中，人数比例最高的是？（出题单位：山东科技报社 推荐单位：山东学习平台）"
    # three = session.query(Bank).filter_by(content=content).all()
    # print(len(three))
    # options=  "A和O A和B AB和O B和O"
    # answer = "A"
    # t = Bank(content=content, options=options, answer=answer)
    # session.add(t)
    # session.commit()



    
    