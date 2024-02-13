from flask import *

app = Flask(__name__)


@app.route('/<tl>')
@app.route('/index/<tl>')
def ind(tl="подстановка "):
    return render_template('index.html', tl=tl)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
