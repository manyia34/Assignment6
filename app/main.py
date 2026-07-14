from fastapi import FastAPI
# =========================================
# Importing routes from Book_routers.py 
# =========================================
from app.routers.book_routes import router as books_router

app = FastAPI(
    title="Library API",
    description="A modular FastAPI CRUD application",
    version="1.0.0"
)

# ==========================================
# Including books_routes in app instance
# =========================================
app.include_router(books_router)

@app.get('/',tags=["Root"])
def home():
    return {
        "message" : "Welcome the Library"
    }
