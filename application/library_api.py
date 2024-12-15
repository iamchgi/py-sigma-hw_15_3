
from http import HTTPStatus

from flask import request, jsonify, Response, make_response, render_template
from flask_restful import Resource
from six import string_types

from application.application import LibraryRepository
from templates.templates import create_html_list_all, create_html_list_one, create_html_info, create_html_new, \
    create_html_action

library_repo = LibraryRepository

class New(Resource):
    def get(self):
        return Response(create_html_new(), HTTPStatus.OK, mimetype='text/html')

class Action(Resource):
    def get(self, book_id):
        return Response(create_html_action(book_id), HTTPStatus.OK, mimetype='text/html')

    def post(self):
        return create_html_info(request.json)

    def put(self):
        return create_html_info(request.json)

    def delete(self):
        return create_html_info(request.json)

class Info(Resource):
    def get(self):
        count = library_repo.get_count_books()
        return Response(create_html_info(["Це Бібліотека","Кількість книг:",count]), HTTPStatus.OK, mimetype='text/html')

class BookList(Resource):                                    # репрезентація ресурсу список книг
    def get(self) -> Response:                                  # отримати список всіх студентів - http_calls - students.http
        list_all = library_repo.get_all_books()
        return Response(create_html_list_all(list_all), HTTPStatus.OK, mimetype='text/html')
        # return jsonify(library_repo.get_all_books())

    def post(self) -> Response:
        result = library_repo.insert_new_book(request.get_json())   # додати нового студента

        if not result:
            return make_response(jsonify("Failed to insert!"), HTTPStatus.INTERNAL_SERVER_ERROR)

        return make_response(jsonify("Created"), HTTPStatus.CREATED)


class Book(Resource):  # репрезентація ресурсу студент
    def get(self, book_id: int) -> Response:  # отримати дані студента
        book = library_repo.get_book_by_id(book_id)
        return Response(create_html_list_one(book), HTTPStatus.OK, mimetype='text/html')
        # return make_response(jsonify(library_repo.get_book_by_id(book_id)), HTTPStatus.OK)

    def put(self, book_id: int) -> Response:  # змінити дані студента

        try:
            is_success = library_repo.update_book_by_id(
                book_id=book_id,
                data=request.get_json(),
            )

            if not is_success:
                return make_response(f"Student failed to update", HTTPStatus.INTERNAL_SERVER_ERROR)

            return make_response(f"Student updated!", HTTPStatus.OK)

        except ValueError as ex:
            print(ex)
            return make_response(f"Student not found", HTTPStatus.NOT_FOUND)
        except Exception as err:
            print(err)
            return make_response(f"Error updating student -> {err}", HTTPStatus.INTERNAL_SERVER_ERROR)

    def delete(self, book_id: int) -> Response:  # видалити дані студента
        try:
            deleted_book, is_success = library_repo.delete_book_by_id(
                book_id=book_id,
            )

            if not is_success:
                return make_response(
                    f"Failed to delete Book with ID {book_id}",
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                )

            return make_response(
                f"Student {deleted_book.title} {deleted_book.author} deleted!",
                HTTPStatus.OK,
            )
        except ValueError as ex:
            print(ex)
            return make_response(f"Book not found", HTTPStatus.NOT_FOUND)
