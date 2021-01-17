from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
import mysql.connector

assignment10 = Blueprint(
    'assignment10', __name__,
    static_url_path='/assignment10',
    template_folder='templates'
)


def interact_db(query, action):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='myflaskapp')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if action == 'commit':
        connection.commit()
        return_value = True

    if action == 'fetch':
        return_value = cursor.fetchall()

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/assignment10')
def users():
    query = "SELECT * FROM users"
    query_result = interact_db(query, 'fetch')
    return render_template('assignment10.html', users_list=query_result)


@assignment10.route('/assignment10', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        user_id = request.form['id']
        email = request.form['email']
        full_name = request.form['full_name']
        query = "INSERT INTO users(id, email, full_name) VALUES ('%s', '%s', '%s')" % (user_id, email, full_name)
        interact_db(query, 'commit')
        return redirect('/assignment10')
    return render_template('assignment10.html')


@assignment10.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        user_id = request.args['id']
        query = "DELETE FROM users WHERE  id='%s';" % user_id
        interact_db(query, 'commit')
        return redirect('/assignment10')
    return 'deleted user'


@assignment10.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        user_id = request.form['id']
        email = request.form['email']
        full_name = request.form['full_name']
        query = "UPDATE users SET email='%s', full_name='%s' WHERE id='%s'" % (email, full_name, user_id)
        interact_db(query, 'commit')
        return redirect('/assignment10')
    return 'update user'
