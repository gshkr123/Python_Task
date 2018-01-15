from flask import render_template

import MySQLdb

from flask import Flask

from flask import render_template, redirect, request

# creating connection Object which will contain SQL Server Connection

app = Flask('__name__')
conn = MySQLdb.connect(host="localhost",
                               user="kumar",
                               passwd="Abcd@123",
                               db="mysql")
c = conn.cursor()
query = "SELECT * from CreditAnalysis where Description LIKE '%PUR%'"
c.execute(query)

data = c.fetchall()

s = "<table style='border:1px solid red'>"
for row in data:
    s = s + "<tr>"
    for x in row:
        s = s + "<td>" + str(x) + "</td>"
    s = s + "</tr>"

conn.close()


@app.route('/')
def main():
    return render_template('index.html', data=home())


@app.route('/home')
def home():
    return """<html>
        <body background src="http://anguerde.com/pics/main/55/402590-white-background.jpg">

        <h2><p><u>This page gives us the details of your Spending in the past 6 months on Purchases made through your Axis Bank Card</u></p></h2>

        <center>""" + s + """</center>

        </body>
        </html>"""

if __name__ == "__main__":
    app.run(port=5003)