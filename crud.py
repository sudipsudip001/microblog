from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreate

def create_book(db: Session, book: BookCreate):
    db_book = Book(
        book_name = book.book_name,
        author_name = book.author_name,
        isbn = book.isbn
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def get_all_books(db: Session):
    return db.query(Book).all()


def update_book(db: Session, book_id: int, book: BookCreate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        return None

    db_book.book_name = book.book_name
    db_book.author_name = book.author_name
    db_book.isbn = book.isbn

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        return None
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}

