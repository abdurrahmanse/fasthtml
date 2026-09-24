# 📚 Reading List

A beautifully designed, luxury SaaS-style web application built with **FastHTML** for collecting books, articles, and resources worth reading. It features a fully responsive design, multi-page routing, and uses SQLite for persistence. By leveraging HTMX, the app delivers seamless, SPA-like partial updates without requiring any complex frontend build steps or JavaScript bundlers.

---

## ✨ Features

- **Luxury UI/UX:** A clean, modern, and highly polished interface mimicking premium SaaS platforms.
- **Fast & Lightweight:** Built on [FastHTML](https://fastht.ml/), keeping the stack simple and blazingly fast.
- **Seamless Interactivity:** Uses [HTMX](https://htmx.org/) for dynamic, partial page updates—no React/Vue needed!
- **Data Persistence:** Out-of-the-box local SQLite database integration.
- **Zero Frontend Build:** No Webpack, Vite, or npm required. Just pure Python and HTML.
- **Modular Architecture:** Cleanly separated concerns with structured routing, services, and repositories.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- `pip` (Python package installer)

### Installation & Running Locally

1. **Clone the repository and navigate into the app directory:**
   ```bash
   cd reading-list
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

5. **Open your browser:**
   Navigate to [http://localhost:5001](http://localhost:5001) to view the app.

---

## 🏗 Project Architecture

The application strictly follows a modular, scalable architecture to separate concerns and ensure maintainability:

```text
reading-list/
├── app/
│   ├── core/                  # Core configurations
│   │   ├── config.py          # Paths and environment-independent configuration
│   │   ├── database.py        # Database connection, schema, and FastHTML app initialization
│   │   └── style.py           # Centralized luxury SaaS CSS styles
│   ├── repositories/          # Database interactions
│   │   └── book_repository.py # Persistence operations (read/write books)
│   ├── services/              # Business logic
│   │   └── book_service.py    # Validation and input normalization rules
│   ├── ui/                    # UI Layer
│   │   ├── components.py      # Reusable HTML fragments and forms (e.g., book_card)
│   │   └── layout.py          # Global HTML layout with navigation and footer
│   └── routes/                # HTTP endpoints and route handlers
│       ├── __init__.py        # Registers all route modules
│       ├── home.py            # Dashboard endpoint (/)
│       ├── books.py           # HTMX API endpoints for CRUD operations
│       ├── about.py           # About page (/about)
│       └── contact.py         # Contact page (/contact)
├── data/                      # Runtime SQLite database (ignored by git)
├── main.py                    # Application entrypoint
└── requirements.txt           # Python dependencies
```

## 🧩 Responsibility Boundaries

To keep the codebase maintainable, the app enforces strict responsibility boundaries:

- **Routes (`app/routes/`):** Coordinate web requests, define HTTP endpoints, and delegate business logic.
- **Services (`app/services/`):** Validate input, execute business rules, and act as the bridge between routes and repositories.
- **Repository (`app/repositories/`):** Handles all database read/write operations. It never renders HTML.
- **UI (`app/ui/`):** Renders FastHTML components, fragments, and global layouts. It contains zero database logic.
- **Core (`app/core/`):** Owns the FastHTML app instantiation, CSS styling tokens, table schemas, and shared constants.
- **Main (`main.py`):** Starts the Uvicorn server and runs the application.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to check out the [issues page](#) if you want to contribute.

## 📝 License

This project is licensed under the MIT License.
