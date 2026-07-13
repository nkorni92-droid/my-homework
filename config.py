# config.py
import os

# Строка подключения к базе данных
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "///"
)
