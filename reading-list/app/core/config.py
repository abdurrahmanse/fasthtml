from pathlib import Path

import os

BASE_DIR = Path(__file__).resolve().parent.parent
data_dir_env = os.environ.get("READING_LIST_DATA_DIR")
DATA_DIR = Path(data_dir_env) if data_dir_env else BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "reading-list.db"
