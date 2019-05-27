# 导入:
from sqlalchemy import Column,Integer, String, Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config

# 创建对象的基类:
Base = declarative_base()

# 定义Bank对象:
class Bank(Base):
    # 表的名字:
    __tablename__ = 'Bank'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    options = Column(Text)
    answer = Column(String(128))

    def __repr__(self):
        return f'\n{self.content}\n{self.options}\t{self.answer.upper()}'

# 初始化数据库连接:
engine = create_engine(Config.DATABASE_URI)

# 创建DBSession类型:
Session = sessionmaker(bind=engine)


if __name__ == "__main__":
    # 创建数据表
    Base.metadata.create_all(engine)
    session = Session()

    one = session.query(Bank).all()
    print(f'题库规模： {len(one)} 题')
    for o in one:
        print(o)

    
    