from pydantic import BaseModel

class BookCreate(BaseModel):
    book_name: str
    author_name: str
    isbn: int

class BookResponse(BaseModel):
    id: int
    book_name: str
    author_name: str
    isbn: int

    class Config:
        orm_mode = True

