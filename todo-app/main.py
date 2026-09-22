"""
FastHTML Todo App
A small full-stack Python web app built with python-fasthtml.

Run with:
    python main.py
Then open http://localhost:5001
"""

from fasthtml.common import *

# ---------------------------------------------------------------------------
# App + database setup
# ---------------------------------------------------------------------------
# fast_app() creates the FastHTML app, the `app.route` shortcut (rt), and,
# because we pass db_file + a table schema, it also gives us back a live
# `fastlite` Table object (todos) and the auto-generated dataclass (Todo).
app, rt, todos, Todo = fast_app(
    "data/todos.db",
    id=int,
    title=str,
    done=bool,
    pk="id",
    hdrs=(
        Style("""
            body { max-width: 700px; margin: 40px auto; font-family: system-ui, sans-serif; }
            .todo-row { display: flex; align-items: center; gap: .5rem; }
            .todo-row.done span { text-decoration: line-through; color: #888; }
            .todo-row span { flex: 1; }
            form.add-form { display: flex; gap: .5rem; margin-bottom: 1.5rem; }
            form.add-form input[type=text] { flex: 1; }
            #todo-list li { list-style: none; }
        """),
    ),
)


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------
def todo_row(todo: Todo):
    "Render a single todo item as an <li> with a toggle checkbox and delete button."
    cls = "todo-row done" if todo.done else "todo-row"
    return Li(
        Div(
            Input(
                type="checkbox",
                checked=todo.done,
                hx_post=f"/toggle/{todo.id}",
                hx_target=f"#todo-{todo.id}",
                hx_swap="outerHTML",
            ),
            Span(todo.title),
            Button(
                "Delete",
                hx_delete=f"/todos/{todo.id}",
                hx_target=f"#todo-{todo.id}",
                hx_swap="outerHTML",
                hx_confirm="Delete this todo?",
                cls="secondary",
            ),
            cls=cls,
        ),
        id=f"todo-{todo.id}",
    )


def todo_list():
    "Render the full <ul> list of todos, most recently added first."
    items = todos(order_by="id desc")
    return Ul(*[todo_row(t) for t in items], id="todo-list")


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@rt("/")
def index():
    return Titled(
        "Todo List",
        Form(
            Input(type="text", name="title", placeholder="What needs doing?", required=True),
            Button("Add"),
            hx_post="/todos",
            hx_target="#todo-list",
            hx_swap="afterbegin",
            hx_on__after_request="this.reset()",
            cls="add-form",
        ),
        todo_list(),
    )


@rt("/todos")
def post(title: str):
    "Create a new todo and return just the new <li> so htmx can insert it."
    todo = todos.insert(title=title, done=False)
    return todo_row(todo)


@rt("/toggle/{id}")
def post(id: int):
    "Flip a todo's done state and return the updated row."
    todo = todos[id]
    todo.done = not todo.done
    todos.update(todo)
    return todo_row(todo)


@rt("/todos/{id}")
def delete(id: int):
    "Delete a todo. Returning an empty string removes the row via hx-swap."
    todos.delete(id)
    return ""


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------
serve()
