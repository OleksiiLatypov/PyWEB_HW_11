from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()  # для визначення структури класів та успадкування від нього


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    lastname = Column(String, index=True, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)
    birthday = Column(DateTime, index=True, nullable=True)
    additional_info = Column(String, index=True)
    created_at = Column('created_at', DateTime, default=func.now())
    updated_at = Column('updated_at', DateTime, default=func.now())
