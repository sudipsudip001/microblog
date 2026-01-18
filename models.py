from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "bookstore"

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, nullable=False)
    author_name = Column(String, nullable=False)
    isbn = Column(Integer, unique=True, nullable=False)

