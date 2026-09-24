from app.core.database import rt
from app.services.book_service import normalize_book
from app.repositories.book_repository import add_book, update_book_status, delete_book
from app.ui.components import book_card, error_message

@rt("/books", methods=["POST"])
def create_book(title: str, author: str, url: str = "", status: str = "unread"):
    try:
        book_data = normalize_book(title, author, url, status)
        new_book = add_book(**book_data)
        return book_card(new_book), error_message("", hx_swap_oob="true")
    except ValueError as e:
        return error_message(str(e), hx_swap_oob="true")


@rt("/books/{book_id}/status/{status}", methods=["POST"])
def change_status(book_id: int, status: str):
    try:
        normalize_book("valid", "valid", "", status)
        return book_card(update_book_status(book_id, status))
    except ValueError as e:
        # In a real app we might want to show this error somewhere, 
        # but for status change it usually comes from the UI so it should be valid.
        return error_message(str(e), hx_swap_oob="true")


@rt("/books/{book_id}", methods=["DELETE"])
def remove_book(book_id: int):
    delete_book(book_id)
    return ""
