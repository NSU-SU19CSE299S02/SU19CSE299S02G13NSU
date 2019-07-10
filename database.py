import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import UserMixin

Base = declarative_base()




#Always stay at the end of the file
engine = create_engine('sqlite:///health.db')
Base.metadata.create_all(engine)