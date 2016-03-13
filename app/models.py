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


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(512), unique=False)
    address = Column(String(512), unique=False)
    description = Column(String(512), unique=False)
    image_url = Column(String(2083), unique=True)
    latitude = Column(String(16), unique=True)
    longitude = Column(String(16), unique=True)
    phone_number = Column(String(16), unique=True)
    subcategory = Column(String(16), unique=True)
    website = Column(String(2083), unique=True)
    postal_code = String(16)

    def __init__(self, name, address, description, image_url, latitude, longitude, phone_number, subcategory, website, postal_code):
        self.name = name
        self.address = address
        self.description = description
        self.image_url = image_url
        self.latitude = latitude
        self.longitude = longitude
        self.phone_number = phone_number
        self.subcategory = subcategory
        self.website = website
        self.postal_code = postal_code

    def __repr__(self):
        return '<Restaurant %r>' % (self.name)
