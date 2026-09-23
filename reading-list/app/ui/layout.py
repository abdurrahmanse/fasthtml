from fasthtml.common import A, Body, Div, Footer, Head, Header, Html, Main, Meta, P, Title
from app.core.database import app


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
            Main(content_element, cls="main-section-container"),
            Footer(P("A quiet place for the next thing worth reading."), cls="site-footer"),
            cls="page-shell",
        ),
    )
