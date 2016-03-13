from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String(512), unique=False)
    atPlace = Column(String(512), unique=False)
    atTime = Column(DateTime, unique=False)
    circa = Column(DateTime, unique=False)
    illustrate = Column(String(512), unique=False)
    inSpace = Column(String(512), unique=False)
    involved = Column(String(512), unique=False)
    involvedAgent = Column(String(512), unique=False)
    url = Column(String(2083), unique=True)

    def __init__(self, name=None, atPlace=None, atTime=None, circa=None, illustrate=None, inSpace=None, involved=None, involvedAgent=None, url=None):
        self.name = name
        self.atPlace = atPlace
        self.atTime = atTime
        self.circa = circa
        self.illustrate = illustrate
        self.inSpace = inSpace
        self.involved = involved
        self.involvedAgent = involvedAgent
        self.url = url

    def __repr__(self):
        return '<Event %r>' % (self.name)



'''

name
address
description
image (URL)
latitude
longitude
phone number
subcategory (ex: desert, bar)
website
postal code
'''
