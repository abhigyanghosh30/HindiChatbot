#!/usr/bin/python3
import botdata  as bd
import re
import random
import datetime
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///calendar.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime,default=datetime.date.today())
    start_time = Column(DateTime)
    end_time = Column(DateTime)


    def __repr__(self):
        return "Appointment(Date=%s StartTime=%s EndTime%s)" % (self.date, self.start_time, self.end_time)

def schedule(date, start_time, end_time):
    pass

def process_input(sentence):
    pass

if __name__ == "__main__":
    print(random.choice(bd.initials))
    while True:
        input_text = input(">: ")

        keyword = ""        # keyword 
        precedence = 0      # precendence
        key_position = -1   # position of the keyword in the keywords

        for i in range(0,len(bd.keywords)):
            if bd.keywords[i][0] in input_text and bd.keywords[i][1] > precedence:
                precedence = bd.keywords[i][1]
                keyword = bd.keywords[i][0]
                key_position = i

        for i in range(0,len(bd.keywords[key_position][2])):
            pattern = bd.keywords[key_position][2][0]
            print(re.split(pattern,input_text))
            
