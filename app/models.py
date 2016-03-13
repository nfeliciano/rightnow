from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    subcategory = Column(String(512))
    name = Column(String(512), unique=False)
    address = Column(String(512))
    description = Column(String(512))
    latitude = Column(String(16))
    longitude = Column(String(16))
    postal_code = Column(String(16))
    price_range = Column(String(32))
    ticket_availability = Column(Boolean)
    date_header = Column(String(512))
    start_date_time = Column(DateTime)
    end_date_time = Column(DateTime)

    def __init__(self, subcategory, name, address, description, latitude, longitude, postal_code, price_range, ticket_availability, date_header, start_date_time, end_date_time):
        self.subcategory = subcategory
        self.name = name
        self.address = address
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.postal_code = postal_code
        self.price_range = price_range
        self.ticket_availability =  ticket_availability
        self.date_header = date_header
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time



    def __repr__(self):
        return '<Event %r>' % (self.name)


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(512), unique=False)
    address = Column(String(512))
    description = Column(String(512))
    image_url = Column(String(2083))
    latitude = Column(String(16))
    longitude = Column(String(16))
    phone_number = Column(String(16))
    subcategory = Column(String(16))
    website = Column(String(2083))
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


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String(512), unique=False)
    address = Column(String(512))
    description = Column(String(512))
    image_url = Column(String(2083))
    latitude = Column(String(16))
    longitude = Column(String(16))
    phone_number = Column(String(16))
    subcategory = Column(String(16))
    website = Column(String(2083))
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
        return '<Activity %r>' % (self.name)
