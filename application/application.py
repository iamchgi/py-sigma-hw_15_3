"""
Модуль - бізнес-модель - застосування БД - робота з полями БД
Логіка може бути будь-яка, на ВАШУ думку.
Пу суті - маємо сценарій дій / операцій над структурою даних "студент"

"""

from typing import Tuple

from dao.database import ORM_DATABASE
from models.book import BookDBModel
from models.dto import BookDTO


class LibraryRepository:

    @staticmethod
    def get_count_books():
        return BookDBModel.query.count()

    @classmethod
    def get_all_books(cls) -> tuple[BookDTO]:  # отримати усіх студентів з БД
        db_result = BookDBModel.query.all()  # метод.query.all - забезпечує доступ до полів моделі БД
        result = []
        for db_row in db_result:  # type : StudentDBModel - генератор
            result.append(
                BookDTO(
                    id=db_row.id,
                    title=db_row.title,
                    author=db_row.author,
                    publisher=db_row.publisher,
                    genre=db_row.genre,
                    published=db_row.published,
                )
            )
        return tuple(result)  # результат повертаємо в кортежі: упорядкована незмінна колекція

    @classmethod
    def get_book_by_id(cls, book_id: int) -> BookDTO:  # отримати з БД книгу за id
        db_row = BookDBModel.query.filter_by(id=book_id).first()
        if not db_row:
            return None
            # raise ValueError(f"Not found Book {book_id}")

        return BookDTO(
            id=db_row.id,
            title=db_row.title,
            author=db_row.author,
            publisher=db_row.publisher,
            genre=db_row.genre,
            published=db_row.published,
        )

    @classmethod
    def insert_new_book(cls, book_data: dict) -> bool:  # додати нового студента
        new_book = BookDBModel(**book_data)

        try:
            ORM_DATABASE.session.add(new_book)
            ORM_DATABASE.session.commit()
            return True
        except Exception as ex:
            print(ex)
            ORM_DATABASE.session.rollback()
            return False

    @classmethod
    def update_book_by_id(cls, book_id: int, data: dict) -> bool:  # модифікувати інформацію про студента з id
        try:
            result = ORM_DATABASE.session.query(BookDBModel).filter(
                BookDBModel.id == book_id
            ).update(data)

            if not result:
                ORM_DATABASE.session.rollback()
                return False

            ORM_DATABASE.session.commit()
            return True
        except Exception as ex:
            print(ex)
            ORM_DATABASE.session.rollback()
            return False

    @classmethod
    def delete_book_by_id(cls, book_id: int) -> Tuple[BookDTO, bool]:  # видалити інформацію про студента з id
        try:
            db_row = BookDBModel.query.filter_by(id=book_id).first()
            if not db_row:
                raise ValueError(f"Not found Student with Id {book_id}")

            deleted_book = BookDTO(
                id=db_row.id,
                title=db_row.title,
                author=db_row.author,
                publisher=db_row.publisher,
                genre=db_row.genre,
                published=db_row.published,
            )
            ORM_DATABASE.session.query(BookDBModel).filter(
                BookDBModel.id == book_id
            ).delete()

            ORM_DATABASE.session.commit()
            return deleted_book, True
        except ValueError:
            raise
        except Exception as ex:
            print(ex)
            ORM_DATABASE.session.rollback()
            return None, False
