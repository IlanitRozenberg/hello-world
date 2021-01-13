from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = '123'


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
    return render_template('assignment9.html', search_term=search, username=username,)


if __name__ == '__main__':
    app.run()
