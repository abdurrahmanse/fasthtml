from fasthtml.common import A, Body, Div, Footer, Head, Header, Html, Main, P, Section, Span, Titled, Title

from .components import book_card, book_form
from .database import app, rt
from .repository import add_book, delete_book, list_books, update_book_status
from .services import normalize_book


@rt("/")
def index():
    saved_books = list_books()
    total_books = len(saved_books)
    reading_count = sum(1 for book in saved_books if book.status == "reading")
    finished_count = sum(1 for book in saved_books if book.status == "finished")
    unread_count = total_books - reading_count - finished_count

    return Html(
        Head(Title("Reading List")),
        Body(
            Header(
                Div(
                    Div(
                        P("PERSONAL LIBRARY", cls="eyebrow"),
                        A("Refresh", href="/", cls="topbar-link"),
                        cls="topbar",
                    ),
                    Div(
                        Titled("Reading List", "Collect good ideas. Keep them moving."),
                        Div(
                            Span("All books", cls="pill"),
                            Span(f"{total_books} total", cls="pill muted"),
                            cls="header-pills",
                        ),
                        cls="intro",
                    ),
                    cls="site-header",
                )
            ),
            Main(
                Div(
                    Div(
                        Div(
                            P("Books", cls="stat-label"),
                            P(str(total_books), cls="stat-value"),
                            cls="stat-card",
                        ),
                        Div(
                            P("Reading", cls="stat-label"),
                            P(str(reading_count), cls="stat-value"),
                            cls="stat-card accent",
                        ),
                        Div(
                            P("Finished", cls="stat-label"),
                            P(str(finished_count), cls="stat-value"),
                            cls="stat-card success",
                        ),
                        Div(
                            P("Unread", cls="stat-label"),
                            P(str(unread_count), cls="stat-value"),
                            cls="stat-card subtle",
                        ),
                        cls="stats-grid",
                    ),
                    Div(
                        Section(
                            P("Add a title", cls="section-label"),
                            book_form(),
                            cls="add-panel",
                        ),
                        Section(
                            Div(
                                Div(
                                    P("Your collection", cls="section-label"),
                                    P(f"{total_books} titles", cls="book-count"),
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
                    cls="dashboard-shell",
                ),
                cls="main-shell",
            ),
            Footer(P("A quiet place for the next thing worth reading."), cls="site-footer"),
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
