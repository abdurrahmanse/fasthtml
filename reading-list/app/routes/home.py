from fasthtml.common import Div, H1, P, Section, Span, A
from app.core.database import rt
from app.repositories.book_repository import list_books
from app.ui.layout import layout
from app.ui.components import book_card, book_form

@rt("/")
def index():
    saved_books = list_books()
    total_books = len(saved_books)
    reading_count = sum(1 for book in saved_books if book.status == "reading")
    finished_count = sum(1 for book in saved_books if book.status == "finished")
    unread_count = total_books - reading_count - finished_count

    header_intro = Div(
        H1("Reading List"),
        P("Collect good ideas. Keep them moving."),
        Div(
            Span("All books", cls="pill"),
            Span(f"{total_books} total", cls="pill muted"),
            cls="header-pills",
        ),
        cls="intro",
    )

    content = Div(
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
    )

    return layout("Reading List", content, header_intro)
