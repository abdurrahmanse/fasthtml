VALID_STATUSES = {"unread", "reading", "finished"}


def normalize_book(title: str, author: str, url: str, status: str) -> dict[str, str]:
    clean_title = title.strip()
    clean_author = author.strip()
    clean_url = url.strip()
    clean_status = status.strip().lower()

    if not clean_title:
        raise ValueError("A title is required.")
    if not clean_author:
        raise ValueError("An author is required.")
    if clean_status not in VALID_STATUSES:
        raise ValueError("Choose a valid reading status.")

    return {
        "title": clean_title,
        "author": clean_author,
        "url": clean_url,
        "status": clean_status,
    }
