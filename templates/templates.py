from flask import render_template

def create_html_new():
    return render_template('new.html')

def create_html_edit(book):
    return render_template('edit.html', book=book)

def create_html_info(list_all):
    return render_template('info.html', data=list_all)

def create_html_list_one(item) -> str:
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
                 .format(i, item.id, item.title, item.author, item.publisher, item.genre, item.published,edit_button,delete_button))
        i += 1
    html += "</table>"
    return html