from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


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
    return render_template('assignment8.html', Hobbies=['Reading', 'Playing with my dog',
                                                        'Spending time with family and friends'], )


if __name__ == '__main__':
    app.run()
