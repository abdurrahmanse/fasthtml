from app.core.database import rt
from app.services.book_service import normalize_book
from app.repositories.book_repository import add_book, update_book_status, delete_book
from app.ui.components import book_card

@rt("/books", methods=["POST"])
def create_book(title: str, author: str, url: str = "", status: str = "unread"):
    book_data = normalize_book(title, author, url, status)
    return book_card(add_book(**book_data))


@rt("/books/{book_id}/status/{status}", methods=["POST"])
def change_status(book_id: int, status: str):
    normalize_book("valid", "valid", "", status)
    return book_card(update_book_status(book_id, status))


@rt("/books/{book_id}", methods=["DELETE"])
def remove_book(book_id: int):
    delete_book(book_id)
    return ""
