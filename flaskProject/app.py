from flask import Flask, redirect, url_for, render_template, request, session, make_response
from assignment10.app import assignment10, interact_db
import json

app = Flask(__name__)
app.secret_key = '123'
app.register_blueprint(assignment10)


@app.route('/contacts')
@app.route('/contacts/')
def contacts_func():
    return render_template('contacts.html')


@app.route('/contact-me')
@app.route('/contact-me/')
def contact_me_func():
    return render_template('contact_me.html')


@app.route('/home')
@app.route('/home/')
@app.route('/')
def home_func():
    return render_template('CV.html')


@app.route('/assignment8')
@app.route('/assignment8/')
def assignment8_func():
    return render_template('assignment8.html', Hobbies=[
        'Reading', 'Playing with my dog', 'Spending time with family and friends',
    ], )


@app.route('/assignment9/', methods=['GET', 'POST'])
@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    username = ''
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        if username == '':
            session['logged_in'] = False
        else:
            session['logged_in'] = True
    search = ''
    if 'search' in request.args:
        search = request.args['search']
    return render_template('assignment9.html', search_term=search, username=username, )


@app.route("/assignment11/users")
@app.route("/assignment11/users/")
def assignment11_func():
    query = "SELECT * FROM users"
    output = interact_db(query, 'fetch')
    for x in range(len(output)):
        temp = output[x]
        output[x] = {"id": temp[0], "full name": temp[2], "email": temp[1]}
    return make_response({"USERS": output}, 200)


@app.route("/assignment11/users/selected")
@app.route("/assignment11/users/selected/")
@app.route("/assignment11/users/selected/<int:uid>")
def assignment11_func2(uid=1):
    query = "SELECT * FROM users WHERE id=%s" % uid
    output = interact_db(query, 'fetch')
    for x in range(len(output)):
        temp = output[x]
        output[x] = {"id": temp[0], "full name": temp[2], "email": temp[1]}
    if len(output) == 0:
        return make_response({"ERROR": "INVALID ID"}, 200)
    return make_response(output[0], 200)


if __name__ == '__main__':
    app.run()
