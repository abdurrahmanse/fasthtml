from .database import Book, books


def list_books():
    """Return saved books with unread items first and newest items first."""
    return books(order_by="status, id desc")


def add_book(title: str, author: str, url: str, status: str) -> Book:
    return books.insert(title=title, author=author, url=url, status=status)


def update_book_status(book_id: int, status: str) -> Book:
    book = books[book_id]
    book.status = status
    books.update(book)
    return book


def delete_book(book_id: int) -> None:
    books.delete(book_id)
