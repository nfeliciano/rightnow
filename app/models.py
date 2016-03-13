from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    atPlace = Column(String(512), unique=False)
    atTime = Column(DateTime, unique=False)
    circa = Column(DateTime, unique=False)
    illustrate = Column(String(512), unique=False)
    inSpace = Column(String(512), unique=False)
    involved = Column(String(512), unique=False)
    involvedAgent = Column(String(512), unique=False)
    url = Column(String(2083), unique=True)


    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
