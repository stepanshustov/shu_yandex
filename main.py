from flask import *

app = Flask(__name__)


@app.route('/')
def mn():
    return "Миссия Колонизация Марса"


@app.route('/index/')
def ind():
    return "И на Марсе будут яблони цвести!"


@app.route('/a/')
def fun():
    user = "Ученик Яндекс.Лицея"
    return render_template('f.html', title='Домашняя страница',
                           username=user)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
