raw_books = [
    {"book_code": "B301", "category": "science", "price": 185000, "status": "available"},
    {"book_code": " b101 ", "category": "novel", "price": 95000, "status": "available"},
    {"book_code": "B202", "category": "history", "price": 240000, "status": "borrowed"},
    {"book_code": "B102", "category": "novel", "price": 120000, "status": "lost"},
    {"book_code": "B302", "category": "science", "price": 210000, "status": "available"}
]
def clean_and_validate_books(books_list):
    valid_books = []
    for book in books_list:
        code = book.get("book_code", "").strip().upper()
        book["book_code"] = code
        if len(code) > 1 and code[0] == 'B' and code[1:].isdigit():
            valid_books.append(book)
    return valid_books
def search_books(books_list, max_price, status=None):
    result = []
    for book in books_list:
        if book["price"] <= max_price:
            if status is None or book["status"] == status:
                result.append(book)
    return result

def sort_books_by_price_desc(books_list):
    n = len(books_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if books_list[j]["price"] < books_list[j + 1]["price"]:
                books_list[j], books_list[j + 1] = books_list[j + 1], books_list[j]
    return books_list