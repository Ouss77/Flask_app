from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import mysql.connector
from prettytable import from_db_cursor
from mysql.connector.errors import Error

app = Flask(__name__)

conDatabase = {
            'host': '127.0.0.1',
            'database': 'employees',
            'user': 'root',
            'password': 'intellia@2022'
        }
try:
  db = mysql.connector.connect(**conDatabase)
  print("the database is connected ")
except Error as error:
  print("Error!")
  print(error)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again !'
        else:
            # flashes on successful login
            flash('You were successfully logged in')
            return redirect(url_for('condition'))
    return render_template('login.html', error=error)
@app.route('/hist')
def initial():
    return render_template('hist.html')
@app.route('/hist', methods=['POST'])
def condition():
    if request.method == 'POST':
        variable = request.form['variable']
        #date_task = request.form['date_task']
        cur = db.cursor()
        query1 = "SELECT * FROM intellia where lots = (%s)"
        #query2 = "SELECT * FROM intellia where date = (%s)"
        cur.execute(query1, (variable,))
        #cur.execute(query2, (date_task,))
        userDetails = cur.fetchall()
        return render_template('hist.html', userDetails=userDetails)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
