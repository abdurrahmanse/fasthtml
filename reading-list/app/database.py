from fasthtml.common import fast_app

from .config import DATA_DIR, DATABASE_PATH
from .style import css

DATA_DIR.mkdir(exist_ok=True)

app, rt, books, Book = fast_app(
    str(DATABASE_PATH),
    pico=False,
    hdrs=(css,),
    tbls={
        "books": {
            "id": int,
            "title": str,
            "author": str,
            "url": str,
            "status": str,
            "pk": "id",
        }
    },
)
