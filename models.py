# models.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    
    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)

class Subject(Base):
    __tablename__ = "subject"
    
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String, nullable=False)

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True)
    user_email = Column(String, nullable=False)
    subject_id = Column(Integer)

class Teacher(Base):
    __tablename__ = "teacher"
    
    teacher_id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    group_id = Column(Integer)

# Другие таблицы (если нужны для тестов)
class Species(Base):
    __tablename__ = "species"
    
    species_id = Column(Integer, primary_key=True)
    type_id = Column(Integer)
    species_name = Column(String, nullable=False)
    species_amount = Column(Integer)
    date_start = Column(Date)
    species_status = Column(String, nullable=False)

class Place(Base):
    __tablename__ = "places"
    
    place_id = Column(Integer, primary_key=True)
    place_name = Column(String, nullable=False)
    place_size = Column(Numeric)
    place_date_start = Column(DateTime, nullable=False)