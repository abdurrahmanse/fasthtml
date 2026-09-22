from fasthtml.common import A, Article, Body, Div, Footer, Head, Header, Html, Main, P, Section, Titled, Title, Ul

from .components import book_card, book_form
from .database import app, rt
from .repository import add_book, delete_book, list_books, update_book_status
from .services import normalize_book


@rt("/")
def index():
    saved_books = list_books()
    return Html(
        Head(Title("Reading List")),
        Body(
            Header(
                Div(
                    P("PERSONAL LIBRARY", cls="eyebrow"),
                    Titled("Reading List", "Collect good ideas. Keep them moving."),
                    cls="intro",
                ),
                cls="site-header",
            ),
            Main(
                Section(
                    P("Add a title", cls="section-label"),
                    book_form(),
                    cls="add-panel",
                ),
                Section(
                    Div(
                        Div(
                            P("Your collection", cls="section-label"),
                            P(f"{len(saved_books)} titles", cls="book-count"),
                            cls="section-heading",
                        ),
                        A("Refresh", href="/", cls="refresh-link"),
                        cls="collection-header",
                    ),
                    Div(*[book_card(book) for book in saved_books], id="book-list", cls="book-list"),
                    cls="collection-panel",
                ),
                cls="content-grid",
            ),
            Footer(P("A quiet place for the next thing worth reading.")),
            cls="page-shell",
        ),
    )


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
