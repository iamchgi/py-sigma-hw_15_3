from http import HTTPStatus

from flask import request, jsonify, Response, make_response
from flask_restful import Resource

from application.application import LibraryRepository
from templates.templates import create_html_list_all, create_html_list_one, create_html_info, create_html_new, \
    create_html_edit

library_repo = LibraryRepository


class New(Resource):
    def get(self):
        return Response(create_html_new(), HTTPStatus.OK, mimetype='text/html')


class Edit(Resource):
    def get(self, book_id):
        book = library_repo.get_book_by_id(book_id)
        if book is not None:
            return Response(create_html_edit(book), HTTPStatus.OK, mimetype='text/html')

    def post(self, book_id):
        form = request.form.to_dict()
        if form['_method']:
            if form['_method'] == 'delete':
                book = Book()
                return book.delete(book_id)
            elif form['_method'] == 'edit':
                book = library_repo.get_book_by_id(book_id)
                if book is not None:
                    return Response(create_html_edit(book), HTTPStatus.OK, mimetype='text/html')
        return make_response(f"Error get method -> {form}", HTTPStatus.INTERNAL_SERVER_ERROR)


class Info(Resource):
    def get(self):
        count = library_repo.get_count_books()
        return Response(create_html_info(["Це Бібліотека", "Кількість книг:", count]), HTTPStatus.OK,
                        mimetype='text/html')


class BookList(Resource):  # репрезентація ресурсу список книг
    def get(self) -> Response:  # отримати список всіх студентів - http_calls - students.http
        list_all = library_repo.get_all_books()
        return Response(create_html_list_all(list_all), HTTPStatus.OK, mimetype='text/html')
        # return jsonify(library_repo.get_all_books())

    def post(self) -> Response:
        result = library_repo.insert_new_book(request.form.to_dict())  # додати нову книгу
        # result = library_repo.insert_new_book(request.get_json())   # додати нову книгу
        if not result:
            return make_response(jsonify("Failed to insert!"), HTTPStatus.INTERNAL_SERVER_ERROR)
        return make_response(jsonify("Created"), HTTPStatus.CREATED)


class Book(Resource):  # репрезентація ресурсу книга
    def get(self, book_id: int) -> Response:  # отримати дані книги
        book = library_repo.get_book_by_id(book_id)
        if book is not None:
            return Response(create_html_list_one(book), HTTPStatus.OK, mimetype='text/html')
        # return make_response(jsonify(library_repo.get_book_by_id(book_id)), HTTPStatus.OK)
        else:
            return make_response(jsonify(f"Failed to found! Book by id {book_id}"), HTTPStatus.INTERNAL_SERVER_ERROR)

    def post(self, book_id: int) -> Response:
        try:
            is_success = library_repo.update_book_by_id(
                book_id=book_id,
                data=request.form.to_dict(),
            )
            if not is_success:
                return make_response(f"Book failed to update", HTTPStatus.INTERNAL_SERVER_ERROR)
            return make_response(f"Book updated!", HTTPStatus.OK)
        except ValueError as ex:
            print(ex)
            return make_response(f"Book not found", HTTPStatus.NOT_FOUND)
        except Exception as err:
            print(err)
            return make_response(f"Error updating book -> {err}", HTTPStatus.INTERNAL_SERVER_ERROR)

    def put(self, book_id: int) -> Response:  # змінити дані книги
        try:
            is_success = library_repo.update_book_by_id(
                book_id=book_id,
                data=request.get_json(),
            )
            if not is_success:
                return make_response(f"Book failed to update", HTTPStatus.INTERNAL_SERVER_ERROR)
            return make_response(f"Book updated!", HTTPStatus.OK)
        except ValueError as ex:
            print(ex)
            return make_response(f"Book not found", HTTPStatus.NOT_FOUND)
        except Exception as err:
            print(err)
            return make_response(f"Error updating book -> {err}", HTTPStatus.INTERNAL_SERVER_ERROR)

    def delete(self, book_id: int) -> Response:  # видалити дані про книгу
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
                f"Книга {deleted_book.title} {deleted_book.author} deleted!",
                HTTPStatus.OK,
            )
        except ValueError as ex:
            print(ex)
            return make_response(f"Book not found", HTTPStatus.NOT_FOUND)
