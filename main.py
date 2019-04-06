#!/usr/bin/python3
import botdata
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
    print(botdata.initials[random%3])
