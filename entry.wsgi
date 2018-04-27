from datetime import datetime
from flask import Flask, render_template, redirect, request
# from Oracle import app
import HTML

app = Flask(__name__)

import pypyodbc

application = Flask(__name__)

# creating connection Object which will contain SQL Server Connection
connection = pypyodbc.connect('Driver={SQL Server};Server=.;Database=Student')  # Creating Cursor

cursor = connection.cursor()


@app.route('/Dash')
def dash():
    cur = cursor.execute("SELECT Pstatus,Medu,Fedu,studytime,Dalc,Walc FROM student_records")
    entries = [dict(Pstatus=row[0], Medu=row[1], Fedu=row[2], studytime=row[3], Dalc=row[4], Walc=row[5]) for row in
               cur.fetchall()]
    return render_template('Dash.html', entries=entries)

connection.close()

if __name__ == "__main__":
    app.run()




# @app.route('/')
# @app.route('/home')
# def home():
#     # return "<html><head><title></title><body>" + s + "</body></html>"
#     return render_template('Dash.html', entries=s)

