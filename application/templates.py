"""
Модуль відповідає за генерацію WEB сторінок
"""

from flask import render_template


# Генерація стрінки для вводу нової книги
def create_html_new() -> str:
    return render_template('new.html')


# Генерація сторінки для редагування книги
def create_html_edit(book) -> str:
    return render_template('edit.html', book=book)


# Сгенерована сторінка відображає інформацію про бібліотеку
def create_html_info(list_all) -> str:
    return render_template('info.html', data=list_all)


def create_html_list_one(item) -> str:
    """
    :param item: книга для відображення на WEB сторінці
    :return: сгенерована сторінка
    """
    # Генеруємо HTML-таблицю
    html = "<table border='1'>\n"
    html += "  <tr><th>ID</th><th>Назва</th><th>Автор</th><th>Видавник</th><th>Жанр</th><th>Рік</th></tr>\n"
    html += ("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n"
             .format(item.id, item.title, item.author, item.publisher, item.genre, item.published))
    html += "</table>"
    html += f"<form action=\"/edit/{item.id}\" method=\"POST\" style=\"display: inline;\">"
    html += "<button type=\"submit\" name=\"_method\" value=\"edit\">Edit</button>"
    html += "<button type=\"submit\" name=\"_method\" value=\"delete\">Delete</button>"
    html += "</form>"
    return html


def create_html_list_all(list_all) -> str:
    """
    :param list_all: список книг для відображення
    :return: сгенерована сторінка
    """
    # Генеруємо HTML-таблицю
    html = "<table border='1'>\n"
    html += ("  <tr><th>№</th><th>ID</th><th>Назва</th><th>Автор</th><th>Видавник</th><th>Жанр</th><th>Рік</th>"
             "<th>EDIT</th><th>DELETE</th></tr>\n")
    i = 1
    for item in list_all:
        edit_button = f"<form action=\"/edit/{item.id}\" method=\"POST\" style=\"display: inline;\">"
        edit_button += "<input type=\"hidden\" name=\"_method\" value=\"edit\">"
        edit_button += "<button type=\"submit\">Edit</button></form>"
        delete_button = f"<form action=\"/edit/{item.id}\" method=\"POST\" style=\"display: inline;\">"
        delete_button += "<input type=\"hidden\" name=\"_method\" value=\"delete\">"
        delete_button += "<button type=\"submit\">DELETE</button></form>"
        html += ("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>"
                 "<td>{}</td><td>{}</td></tr>\n"
                 .format(i, item.id, item.title, item.author, item.publisher, item.genre, item.published, edit_button,
                         delete_button))
        i += 1
    html += "</table>"
    return html
