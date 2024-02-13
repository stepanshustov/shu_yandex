from flask import *

app = Flask(__name__)


def check(st: str):
    st = st.lower()
    if "инженер" in st:
        return 1
    if "техн" in st:
        return 1
    if "програм" in st:
        return 1
    return 2


@app.route('/')
@app.route('/index/<tl>')
@app.route('/index/')
def ind(tl="заголовок"):
    return render_template('base.html', title=tl)


@app.route('/training/<prof>')
def tr(prof):
    return render_template('index.html', number=check(prof), title="mars")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
