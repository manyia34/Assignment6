from typing import Optional
from pydantic import BaseModel

# ===============================
# Pydantic model of Book Create 
# ===============================
class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    language: str

# ===============================
# Pydantic model of Book Update 
# ===============================
class BookUpdate(BaseModel):
    title : str 
    author : str 
    genre : str 
    language : str 

# ================================
# Pydantic model of BookResponse
# ================================
class BookResponse(BaseModel):
    id : int 
    title : str 
    genre : str 
    author : str 
    language : str 
    
# ===============================
# Pydantic model of Book Patch 
# ===============================
class BookPatch(BaseModel):
    title : Optional[str] = None
    author : Optional[str] = None
    genre : Optional[str] = None
    language : Optional[str] = None
    
# =======================================
# Pydantic model of BookAction Response 
# =======================================
class BookActionResponse(BaseModel):
    message : str 
    book : BookResponse