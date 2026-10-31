from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class BookCategory(Base):
    __tablename__ = "book_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    books = relationship("Book", back_populates="category")
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    book_code = Column(String(10), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    book_category_id = Column(Integer, ForeignKey("book_categories.id"))

    category = relationship("BookCategory", back_populates="books")