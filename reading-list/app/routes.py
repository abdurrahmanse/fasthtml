from fasthtml.common import A, Body, Div, Footer, Head, Header, Html, Main, Meta, P, Section, Span, H1, Title

from .components import book_card, book_form
from .database import app, rt
from .repository import add_book, delete_book, list_books, update_book_status
from .services import normalize_book


from fasthtml.common import A, Body, Div, Footer, Head, Header, Html, Main, Meta, P, Section, Span, H1, Title

from .components import book_card, book_form
from .database import app, rt
from .repository import add_book, delete_book, list_books, update_book_status
from .services import normalize_book


def layout(title_text, content_element, header_content=None):
    return Html(
        Head(
            Title(title_text),
            Meta(name="viewport", content="width=device-width, initial-scale=1, viewport-fit=cover"),
            *app.hdrs
        ),
        Body(
            Header(
                Div(
                    Div(
                        P("PERSONAL LIBRARY", cls="eyebrow"),
                        Div(
                            A("Home", href="/", cls="topbar-link"),
                            A("About", href="/about", cls="topbar-link"),
                            A("Contact", href="/contact", cls="topbar-link"),
                            style="display: flex; gap: 1.2rem;"
                        ),
                        cls="topbar",
                    ),
                    header_content,
                    cls="site-header",
                )
            ),
            Main(content_element, cls="main-shell"),
            Footer(P("A quiet place for the next thing worth reading."), cls="site-footer"),
            cls="page-shell",
        ),
    )


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


@rt("/about")
def about():
    header_intro = Div(
        H1("About Me"),
        P("A little bit about the creator."),
        cls="intro",
    )
    content = Div(
        Section(
            P("Hi, I'm the creator of this luxury SaaS reading list."),
            P("I love reading and building fast, responsive web applications. This project is built using FastHTML and pure CSS for a lightweight, beautiful experience.", style="color: var(--muted); margin-top: 1rem; line-height: 1.6;"),
            cls="collection-panel",
            style="padding-bottom: 1.5rem;"
        ),
        cls="dashboard-shell",
        style="max-width: 600px; margin: 0 auto;"
    )
    return layout("About Me - Reading List", content, header_intro)


@rt("/contact")
def contact():
    header_intro = Div(
        H1("Contact"),
        P("Get in touch."),
        cls="intro",
    )
    content = Div(
        Section(
            P("Reach out to me for inquiries or support."),
            P("Email: creator@example.com", style="color: var(--muted); margin-top: 1rem;"),
            A("Send an Email", href="mailto:creator@example.com", cls="button button-primary", style="display: inline-block; margin-top: 1.5rem; text-decoration: none;"),
            cls="collection-panel",
            style="padding-bottom: 1.5rem;"
        ),
        cls="dashboard-shell",
        style="max-width: 600px; margin: 0 auto;"
    )
    return layout("Contact - Reading List", content, header_intro)


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
