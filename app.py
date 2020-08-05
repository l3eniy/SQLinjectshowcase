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
        name = request.form.get('name', '')
        with DatabaseHelper() as database:
            #statement = 'SELECT name, email FROM students WHERE id LIKE "%{0}%";'.format(name)
            #statement = 'SELECT name, email FROM students WHERE id="3" UNION ALL SELECT cardnumber,1 FROM creditcard WHERE "1"="1";'.format(name)
            #statement = 'SELECT name, email FROM students WHERE id LIKE "1" UNION SELECT cardnumber,1 FROM creditcard WHERE "1"="1";'.format(name)
            statement = 'SELECT name, email FROM students WHERE id LIKE "1" order by 2-- -";'.format(name)
            database.insert(statement)
            results = database.select(statement)
            retval = list()
            for result in results:
                retval.append(str(result))
            return '<br>'.join(retval)

# @app.route('/', methods=['GET', 'POST'])
# def query():
#     """Runs a RAW query against the database"""
#     if request.method == 'GET':
#         return render_template('query.html')
#     if request.method == 'POST':
#         username = request.form.get('username', '')
#         password = request.form.get('password', '')
#         with DatabaseHelper() as database:
#             statement_u = 'SELECT password FROM login WHERE username LIKE "%{0}%";'.format(username)
#             database.insert(statement_u)
#             results = database.select(statement_u)
#             print(password)
#             print(str(results[0][0]))
#             if password == str(results[0][0]):
#                 ergebnis = "Success !"
#             else:
#                 ergebnis = "Username or Password wrong !"
#             return '<br>'.join(ergebnis)


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 80)
