from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index/<tl>')
@app.route('/index/')
def ind(tl="заголовок"):
    return render_template('index.html', title=tl)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
