from datetime import datetime
from flask import Flask, render_template, redirect, request
# from Oracle import app
import html5lib
import cx_Oracle
import platform, sys

# print("cx_Oracle version:", cx_Oracle.version)
# print("Oracle client version:", cx_Oracle.clientversion())


app = Flask(__name__)

import pypyodbc

application = Flask(__name__)

# creating connection Object which will contain SQL Server Connection
# connection = pypyodbc.connect('Driver={SQL Server};Server=.;Database=Student')  # Creating Cursor

ip = '129.157.178.26'
port = 1521
SID = 'ORCL'
service_name = 'PDB1.595583066.oraclecloud.internal'
dsn_tns = cx_Oracle.makedsn(ip, port, service_name=service_name)

connection = cx_Oracle.connect(user="GAYATRI", password="PANEERTIKKA", dsn=dsn_tns)


cursor = connection.cursor()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tables')
def table():
    cur = cursor.execute("SELECT Pstatus,Medu,Fedu,Mjob,Fjob,Dalc,Walc,absences,G3 FROM GAYATRI.STUDENT_PROFILES WHERE ROWNUM <= 10")

    entries = [dict(Pstatus=row[0], Medu=row[1], Fedu=row[2], Mjob=row[3], Fjob=row[4], Dalc=row[5], Walc=row[6], absences=row[7], G3=row[8]) for row in
               cur.fetchall()]
    return render_template('tables.html', entries=entries)


@app.route('/dashboard')
def dash():

    return render_template('dashboard.html')

# connection.close()

if __name__ == "__main__":
    app.run()




