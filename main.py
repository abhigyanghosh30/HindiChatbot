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
    name = Column(String(100))


    def __repr__(self):
        return "Appointment(Date=%s StartTime=%s EndTime%s)" % (self.date, self.start_time, self.end_time)

def schedule(date, start_time, end_time, event):
    session = Session()
    # resolving date issues
    if date == "kal":
        date = datetime.date.today() + datetime.timedelta(days=1)
    if date == "aaj":
        date = datetime.date.today()
    if start_time.isdigit:
        start_time = datetime.time(int(start_time),0,0)
    if end_time.isdigit:
        end_time = datetime.time(int(end_time),0,0)

    new_appointment = Appointment(date=date, start_time=start_time, end_time=end_time, name=event)
    session.add(new_appointment)
    session.commit()
    print("Maine schedule mai add kar diyaa hai")

def process_input(sentence):
    precedence = 0      # precendence
    key_position = 0   # position of the keyword in the keywords

    # find the keywords and take the keyword with the maximum precedence value
    for i in range(0,len(bd.keywords)):
        if bd.keywords[i][0] in sentence and bd.keywords[i][1] > precedence:
            precedence = bd.keywords[i][1]
            key_position = i

    for i in range(0,len(bd.keywords[key_position][2])):
        pattern = bd.keywords[key_position][2][i][0]
        if re.search(pattern,sentence):
            split_sentence = re.split(pattern,sentence)
            split_sentence = [ elem for elem in split_sentence if elem != "" ]
            if len(split_sentence) > 1:
                # the pattern matches
                transformations = bd.keywords[key_position][2][i][1]
                if transformations[0][:3] == "def":
                    schedule(split_sentence[0], split_sentence[1],split_sentence[2],split_sentence[3])
                    return
                print(random.choice(transformations).format(s=split_sentence))
                print(pattern)
                print(split_sentence)
            


if __name__ == "__main__":
    print(random.choice(bd.initials))
    while True:
        input_text = input(">: ")
        process_input(input_text)

        


            
