from fasthtml.common import Div, H1, P, Section
from app.core.database import rt
from app.ui.layout import layout

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
