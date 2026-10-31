from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def custom_response(status_code: int, error: str, message: str, data: any):
    return {
        "statusCode": status_code,
        "error": error,
        "message": message,
        "data": data
    }
@app.post("/books")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    category = db.query(models.BookCategory).filter(models.BookCategory.id == book.book_category_id).first()
    if not category:
        return custom_response(400, "Bad Request", "Không tìm thấy thể loại sách", None)
    db_book = db.query(models.Book).filter(models.Book.book_code == book.book_code).first()
    if db_book:
        return custom_response(400, "Bad Request", "Mã sách đã tồn tại", None)
    new_book = models.Book(book_code=book.book_code, price=book.price, book_category_id=book.book_category_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return custom_response(201, None, "Thêm sách mới thành công", {"id": new_book.id})
@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    result_data = []
    
    for b in books:
        result_data.append({
            "id": b.id,
            "book_code": b.book_code,
            "price": b.price,
            "book_category": {
                "id": b.category.id,
                "name": b.category.name
            } if b.category else None
        })
        
    return custom_response(200, None, "Lấy danh sách sách thành công", result_data)
@app.delete("/book-categories/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.BookCategory).filter(models.BookCategory.id == id).first()
    if not category:
        return custom_response(404, "Not Found", "Không tìm thấy thể loại sách", None)
    if len(category.books) > 0:
        return custom_response(400, "Bad Request", "Không thể xóa do vẫn còn sách thuộc thể loại này", None)
    db.delete(category)
    db.commit()
    return custom_response(200, None, "Xóa thể loại sách thành công", None)