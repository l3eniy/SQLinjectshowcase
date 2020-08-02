from flask import Flask, render_template, request, redirect

from logic import initialize_database
from database import DatabaseHelper


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/initialize/')
def initialize():
    initialize_database()
    return redirect(request.referrer, 302)


@app.route('/', methods=['GET', 'POST'])
def query():
    """Runs a RAW query against the database"""
    if request.method == 'GET':
        return render_template('query.html')
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        with DatabaseHelper() as database:
            # statement = 'SELECT * FROM {0} WHERE name LIKE "%{1}%";'.format(table, username)
            statement = 'SELECT * FROM creditcard WHERE name LIKE "%{0}%";'.format(username)
            database.insert(statement)
            results = database.select(statement)
            retval = list()
            for result in results:
                retval.append(str(result))
            return '<br>'.join(retval)


if __name__ == '__main__':
    app.run()
