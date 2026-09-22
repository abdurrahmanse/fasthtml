from fasthtml.common import A, Button, Div, Form, H2, Input, Label, Option, P, Select, Span


def book_card(book):
    status_label = book.status.title()
    action_status = "finished" if book.status == "reading" else "reading"
    action_label = "Mark finished" if book.status == "reading" else "Start reading"

    return Div(
        Div(
            Span(status_label, cls=f"status status-{book.status}"),
            H2(book.title),
            P(f"{book.author}", cls="book-author"),
            A("Open source", href=book.url, target="_blank", cls="source-link") if book.url else None,
            cls="book-copy",
        ),
        Div(
            Button(
                action_label,
                hx_post=f"/books/{book.id}/status/{action_status}",
                hx_target=f"#book-{book.id}",
                hx_swap="outerHTML",
                cls="button button-primary",
            ) if book.status != "finished" else None,
            Button(
                "Remove",
                hx_delete=f"/books/{book.id}",
                hx_target=f"#book-{book.id}",
                hx_swap="outerHTML",
                hx_confirm="Remove this book from your list?",
                cls="button button-quiet",
            ),
            cls="book-actions",
        ),
        id=f"book-{book.id}",
        cls="book-card",
    )


def book_form():
    return Form(
        Div(
            Label("Title", fr="title"),
            Input(id="title", name="title", placeholder="e.g. Atomic Habits", required=True),
            cls="field",
        ),
        Div(
            Label("Author", fr="author"),
            Input(id="author", name="author", placeholder="e.g. James Clear", required=True),
            cls="field",
        ),
        Div(
            Label("Link", fr="url"),
            Input(id="url", name="url", type="url", placeholder="https://..."),
            cls="field",
        ),
        Div(
            Label("Status", fr="status"),
            Select(
                Option("Unread", value="unread", selected=True),
                Option("Reading", value="reading"),
                Option("Finished", value="finished"),
                id="status",
                name="status",
            ),
            cls="field",
        ),
        Button("Add to list", cls="button button-primary button-wide"),
        hx_post="/books",
        hx_target="#book-list",
        hx_swap="afterbegin",
        hx_on__after_request="this.reset()",
        cls="book-form",
    )
