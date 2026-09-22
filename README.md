# FastHTML Todo App

A tiny full-stack Todo List app built with [python-fasthtml](https://www.fastht.ml/),
using SQLite (via `fastlite`) for persistence and [htmx](https://htmx.org/) for
interactivity — no separate frontend framework, no JSON API, no build step.

## Features
- Add a todo
- Toggle a todo done/undone (checkbox, live-updates in place)
- Delete a todo (with confirmation)
- Data persisted to a local SQLite database (`data/todos.db`)
- All updates happen via htmx partial swaps — no full page reloads

## Setup

```bash
cd todo-app
python3 -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Then open http://localhost:5001 in your browser.

The app auto-creates `data/todos.db` and the `todos` table on first run.

## Project structure

```
todo-app/
├── main.py             # App, routes, and HTML rendering (all in one file)
├── requirements.txt    # python-fasthtml + fastlite
├── data/               # SQLite DB lives here (gitignored)
└── README.md
```

## How it works

- `fast_app("data/todos.db", id=int, title=str, done=bool, pk="id")` creates
  the FastHTML app *and* a `todos` fastlite table + `Todo` dataclass in one call.
- Each route returns FT (FastHTML "FastTags") components directly — Python
  objects that render to HTML, e.g. `Li(...)`, `Button(...)`.
- htmx attributes (`hx_post`, `hx_target`, `hx_swap`, ...) tell the browser
  to send AJAX-like requests and swap in the returned HTML fragment instead
  of reloading the whole page.
