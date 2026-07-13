# =========================================
# Importing Files 
# =========================================
from fastapi import APIRouter, HTTPException, status
from typing import Optional

# =========================================
# Import book data from book_data.py
# ==========================================
from app.data.book_data import books

# ==============================================
# import Pydantic model from book_model.py
# ==============================================
from app.models.book_models import (
    BookCreate, BookActionResponse, BookUpdate, BookPatch, BookResponse)

# ========================================================
# Creating a Router  : It is similar to the app instance
# ========================================================
router = APIRouter(
    prefix='/books',
    tags=['Books']
)

# ======================
# Query Parameeter 
# ======================
@router.get('', response_model=list[BookResponse], status_code=status.HTTP_200_OK)
def get_books(genre: Optional[str] = None, language: Optional[str] = None):
    filtered_books = books

    if genre is not None:
        result = []
        for book in filtered_books:
            if book["genre"].lower() == genre.lower():
                result.append(book)
        filtered_books = result

    if language is not None:
        result = []
        for book in filtered_books:
            if book["language"].lower() == language.lower():
                result.append(book)
        filtered_books = result

    return filtered_books

# ==============================
# Get : Book by Book_id
# =============================
@router.get('/{book_id}', response_model=BookResponse, status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=" Book Not Found")


# =============================
# Post : Adding New Book
# =============================
@router.post('', response_model=BookActionResponse, status_code=status.HTTP_201_CREATED)
def add_book(book: BookCreate):
    for existing_book in books:
        if existing_book["title"].lower() == book.title.lower():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Book Already exits !")

    new_id = 0
    for i in books:
        if i["id"] > new_id:
            new_id = i["id"]
    new_id = new_id + 1

    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "language": book.language,
        "internal_note": "Added by admin",
        "created_by": "trainer"
    }

    books.append(new_book)
    return {
        "message": "Book Added Successfully !",
        "book": new_book
    }

# ===============================
# Put : Update the whole Record 
# ==============================
@router.put('/{book_id}', response_model=BookActionResponse, status_code=status.HTTP_200_OK)
def Update_book(book_id: int, book: BookUpdate):
    for existing_book in books:
        if existing_book["id"] == book_id:
            existing_book.update(book.model_dump())
            return {
                "message": "Book Update Successfully !",
                "book": existing_book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book Not Found !")


# ======================================
# Patch : Update the specific field 
# ======================================
@router.patch('/{book_id}', response_model=BookActionResponse, status_code=status.HTTP_200_OK)
def update_patch(book_id: int, book: BookPatch):
    for existing_book in books:
        if existing_book["id"] == book_id:
            if book.title is not None:
                existing_book["title"] = book.title
            if book.author is not None:
                existing_book["author"] = book.author
            if book.genre is not None:
                existing_book["genre"] = book.genre
            if book.language is not None:
                existing_book["language"] = book.language
            return {
                "message" : "Book Update Successfully",
                "book" : existing_book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book Not Found !")

# ============================
# Delete : Remove the book 
# ============================
@router.delete('/{book_id}', response_model=BookActionResponse, status_code=status.HTTP_200_OK)
def delete_book(book_id: int):
    for existing_book in books:
        if existing_book["id"] == book_id:
            books.remove(existing_book)
            return {
                "message": "Book deleted Successfully !",
                "book": existing_book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book Not Found !")
