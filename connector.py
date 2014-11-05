
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from lk_api import ApiWrapper

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/login", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        session['login'] = request.form['login']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return render_template('hello.html')

@app.route("/")
def index():
    if 'login' in session and 'password' in session:
        lk_api = ApiWrapper(session['login'], session['password'])
        return render_template("choice.html", tags = lk_api.get_board_tags(),
                                    cards = lk_api.get_card_type())
        #return 'Logged in as %s' % escape(session['login'])
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(debug=True)