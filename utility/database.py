from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
                        Column, 
                        Integer, 
                        String, 
                        MetaData,
                        Date,
                        Text)
from datetime import datetime

DATABASE_URL = "sqlite:///./business.db"
engine = create_engine(DATABASE_URL, poolclass=QueuePool, connect_args={'check_same_thread': False})
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    legal_name = Column(String(100), nullable=True, default=None)
    address = Column(String(200))
    owner_info = Column(String(200))
    employee_size = Column(Integer, nullable=True, default=0)
    founded_date = Column(Date, default=datetime.now)
    founders = Column(Text, nullable=True, default=None)
    last_funding_type = Column(String(100), nullable=True, default=None)
    phone_number = Column(String(50), unique=True)
    contact_email = Column(String(250), unique=True)

# Create the table in the database
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
