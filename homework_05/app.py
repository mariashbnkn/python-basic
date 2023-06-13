"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask
from flask import render_template

from view.index import index_app

app = Flask(__name__)
app.register_blueprint(index_app, url_prefix="/")

app.config.update(
    SECRET_KEY="42ba97397b44e2296d2a4ejio",
)


@app.get("/about/", endpoint="about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(port=5001, debug=True)

