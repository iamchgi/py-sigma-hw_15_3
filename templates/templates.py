from flask import render_template

def create_html_new():
    return render_template('new.html')

def create_html_action(book_id):
    return render_template('action.html', id=book_id)

def create_html_info(list_all):
    return render_template('info.html', data=list_all)

def create_html_list_one(item) -> str:
    # Генеруємо HTML-таблицю

    html = "<table border='1'>\n"
    html += "  <tr><th>ID</th><th>Назва</th><th>Автор</th><th>Видавник</th><th>Жанр</th><th>Рік</th></tr>\n"
    html += ("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n"
                 .format(item.id, item.title, item.author, item.publisher, item.genre, item.published))
    html += "</table>"
    return html

def create_html_list_all(list_all) -> str:
    # Генеруємо HTML-таблицю
    html = "<table border='1'>\n"
    html += "  <tr><th>№</th><th>ID</th><th>Назва</th><th>Автор</th><th>Видавник</th><th>Жанр</th><th>Рік</th></tr>\n"
    i = 1
    for item in list_all:
        html += ("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n"
                 .format(i, item.id, item.title, item.author, item.publisher, item.genre, item.published))
        i += 1
    html += "</table>"
    return html