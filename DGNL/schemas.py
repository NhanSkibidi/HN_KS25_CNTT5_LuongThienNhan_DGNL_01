from pydantic import BaseModel, Field
class BookCreate(BaseModel):
    book_code: str = Field(..., min_length=4, max_length=10)
    price: float = Field(..., gt=0)
    book_category_id: int
class CategoryResponse(BaseModel):
    id: int
    name: str
class BookResponse(BaseModel):
    id: int
    name : str
    price : float
    status : str