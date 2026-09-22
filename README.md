# Reading List

A beautifully designed, luxury SaaS style FastHTML app for collecting books and articles worth reading. It features responsive design, multi-page routing, and uses SQLite for persistence with HTMX for seamless partial updates—all without a frontend build step.

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

The application follows a modular, scalable architecture to separate concerns:

```text
reading-list/
├── app/
│   ├── core/              # Core configurations
│   │   ├── config.py      # Paths and environment-independent configuration
│   │   ├── database.py    # Database connection, schema, and FastHTML app initialization
│   │   └── style.py       # Centralized luxury SaaS CSS styles
│   ├── repositories/      # Database interactions
│   │   └── book_repository.py # Persistence operations (read/write books)
│   ├── services/          # Business logic
│   │   └── book_service.py    # Validation and input normalization rules
│   ├── ui/                # UI Layer
│   │   ├── components.py  # Reusable HTML fragments and forms (e.g. book_card)
│   │   └── layout.py      # Global HTML layout with navigation and footer
│   └── routes/            # HTTP endpoints and route handlers
│       ├── __init__.py    # Registers all route modules
│       ├── home.py        # Dashboard endpoint (/)
│       ├── books.py       # HTMX API endpoints for CRUD operations
│       ├── about.py       # About page (/about)
│       └── contact.py     # Contact page (/contact)
├── data/                  # Runtime SQLite database, ignored by git
├── main.py                # Application entrypoint
├── requirements.txt       # Python dependencies
└── README.md
```

## Responsibility boundaries

- **Routes** (`app/routes/`) coordinate web requests, HTTP endpoints, and delegate work.
- **Services** (`app/services/`) validate input and enforce business rules.
- **Repository** (`app/repositories/`) reads and writes to the database; it does not render HTML.
- **UI** (`app/ui/`) renders FastHTML fragments and global layouts; it does not write to the database.
- **Core** (`app/core/`) owns the app connection, CSS styling, table schema, and constants.
- **Main** starts the Uvicorn server and runs the application.
