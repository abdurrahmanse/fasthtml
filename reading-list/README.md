# Reading List

A small FastHTML app for collecting books and articles worth reading. It uses SQLite for persistence and htmx for partial updates without a frontend build step.

## Run locally

```bash
cd reading-list
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Open <http://localhost:5001>.

## Project structure

```text
reading-list/
├── app/
│   ├── components.py  # Reusable HTML fragments and the add-book form
│   ├── config.py      # Paths and environment-independent configuration
│   ├── database.py    # Database connection, schema, and FastHTML app object
│   ├── repository.py  # Persistence operations only
│   ├── routes.py      # HTTP endpoints and request/response coordination
│   └── services.py    # Validation and input normalization rules
├── data/              # Runtime SQLite database, ignored by git
├── main.py            # Application entrypoint and visual styling
├── requirements.txt   # Python dependencies
└── README.md
```

## Responsibility boundaries

- **Routes** coordinate web requests and delegate work.
- **Services** validate input and enforce business rules.
- **Repository** reads and writes books; it does not render HTML.
- **Components** render FastHTML fragments; they do not write to the database.
- **Database** owns the app connection and table schema.
- **Main** starts the server and owns page-level styling.
