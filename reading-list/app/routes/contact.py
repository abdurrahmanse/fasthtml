from fasthtml.common import Div, H1, P, Section, A
from app.core.database import rt
from app.ui.layout import layout

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
