

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
def hello_world():  # put application's code here
    return 'Не галасуйте!!!! Це бібліотека!'


if __name__ == '__main__':
    # створення БД Бібліотеки
    init_db(app)
    from application.library_api import BookList, Book, Info, Action, New

    api.add_resource(New, "/new")
    api.add_resource(Action, "/action/<int:book_id>")
    api.add_resource(Info, "/info")
    api.add_resource(BookList, "/library")
    api.add_resource(Book, "/library/<int:book_id>")
    app.run(debug=True)
