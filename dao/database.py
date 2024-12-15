"""
Модуль підключення до бази даних Sqlite Python - фізичне її створення.
Це локальна БД.
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
DB_NAME: str = os.path.join(os.getcwd(), "library.db")         # "фізична" побудова БД в кореневому для api каталозі
CONNECTION_STRING: str = f"sqlite:///{DB_NAME}"

ORM_DATABASE = None


def init_db(app: Flask):
    global ORM_DATABASE
    app.config["SQLALCHEMY_DATABASE_URI"] = CONNECTION_STRING   # побудова полів БД
    # app.config["SECRET_KEY"] = "sUpeRSecr3t!Str1ng"             # захист полів бази даних за SECRET_KEY - бажано мати рандомні паролі

    ORM_DATABASE = SQLAlchemy(app)

    # do not remove imports, they are used implicitly
    from models.book import BookDBModel

    with app.app_context():
        SQL = text("drop table if exists books;")
        ORM_DATABASE.session.execute(SQL)
        ORM_DATABASE.create_all()
        try:
            with open("dao/init.sql", "r", encoding="utf-8") as file:
                SQL = file.read()
                ORM_DATABASE.session.execute(text(SQL))
                ORM_DATABASE.session.commit()
        except FileNotFoundError:
            print("Файл не знайдено!")
        print(SQL)