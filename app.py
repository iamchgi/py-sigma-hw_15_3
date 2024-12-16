"""
Виконав: Григорій Чернолуцький
Homework_15.3

Програмний застосунок «WEB-library», який реалізує WEB-технології
інформаційної взаємодії з Python та бібліотекою flask:
1. Застосунок  реалізовує функціонал WEB – бібліотеки на локальному рівні;
2. Збереження бібліографії про книжки в локальній базі даних;
3. Імплементує додавання, модифікацію, видалення, пошук (за обраною ознакою(id)) та
відображення інформації про бібліографію книжок.

Package Version
------- -------
pip            24.3.1
Flask-CORS     5.0.0
flask-sqlalchemy       3.1.1
flask-restful-swagger  0.20.2
Flask         3.1.0
Flask-RESTful 0.3.10
SQLAlchemy    2.0.36
Jinja2                3.1.4

"""
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful_swagger import swagger
from dao.database import init_db


app = Flask(__name__,template_folder='templates',static_folder='static')
# app.url_map.strict_slashes = False                  # підключає правило URL
api = swagger.docs(Api(app), apiVersion='0.1')      # створення об'єкта api + документація для нього - стандартизований json файл для розробників Frontend
# CORS(app, resources={r"/*": {"origins": "*"}})      # увімкнути CORS (дозволити між сайтові запити)


@app.route('/')
def hello_library():  # put application's code here
    return 'Не галасуйте!!!! Це бібліотека!'


if __name__ == '__main__':
    # створення БД Бібліотеки
    init_db(app)
    from application.library_api import BookList, Book, Info, Edit, New

    api.add_resource(New, "/new")
    api.add_resource(Edit, "/edit/<int:book_id>")
    api.add_resource(Info, "/info")
    api.add_resource(BookList, "/library")
    api.add_resource(Book, "/library/<int:book_id>")
    app.run(debug=True)
