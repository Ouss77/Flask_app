from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import mysql.connector
from mysql.connector.errors import Error

app = Flask(__name__)


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'intellia@2022'
app.config['MYSQL_DB'] = 'employee'

mysql = MySQL(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM employee_data")
    userDetails = cur.fetchall()
    return render_template('users.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
