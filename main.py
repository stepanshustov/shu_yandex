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


@app.route('/list/ol/')
def lt():
    with open("list.json", "rt", encoding="utf8") as f:
        list_ = json.loads(f.read())
    return render_template('list1.html', lt=list_)


@app.route('/list/ul/')
def lt2():
    with open("list.json", "rt", encoding="utf8") as f:
        list_ = json.loads(f.read())
    return render_template('list2.html', lt=list_)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
