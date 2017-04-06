import os
import sys
from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movie_details'
    id = Column(Integer,primary_key=True)
    title = Column(String(250),nullable=False)
    tagline = Column(String(300),nullable=True)
    img_url = Column(String(250),nullable=False)
    trailer = Column(String(250),nullable=False)

engine = create_engine('sqlite:///moviedatabase.db')

Base.metadata.create_all(engine)
    
print("done")
