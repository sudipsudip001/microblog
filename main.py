import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}


@app.get("/all_books")
def read_books(db: Session = Depends(get_db)):
    books = crud.get_all_books(db=db)
    if books is None:
        return HTTPException(status_code=404, detail="No book found")
    return books


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.post("/books", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@app.delete("/delete_books")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db=db, book_id=book_id)


@app.put("/update_books")
async def edit_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.update_book(book_id=book_id, book=book, db=db)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)