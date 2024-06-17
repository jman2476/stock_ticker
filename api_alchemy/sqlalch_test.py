# TODO: The purpose of this document is to build a quick test program in sql alchemy, where I'll connect to a simple test database.

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Float, TEXT, select
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = "test2"

    name = Column('name', String, primary_key=True)
    numb = Column('numb', Integer)
    frac = Column('frac', Float)
    motto = Column('motto', TEXT)

    def __init__ (self, name, numb, frac, motto):
        self.name = name
        self.numb = numb
        self.frac = frac
        self.motto = motto

    def __repr__(self):
        return f'Name: {self.name}, \n Number: {self.numb} \n Decimal: {self.frac} \n Motto: {self.motto}\n\n'



engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# greggory_turnips = Person('Greggory Turnips', 34, 3/4, 'When the sun comes up, grab the turnips!')
# sammy_salami = Person('sammy_salami', 123123, 0.3344443, 'Send a salami to a boy in the army')
# session.add(greggory_turnips)
# session.add(sammy_salami)
# session.commit()


statement = select(Person).where(Person.name=='sammy_salami')

results = session.scalars(statement).one()

print(results)