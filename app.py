from flask import Flask, render_template
import mysql.connector #import du client mysql
import json

#connection au serveur mysql
db = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="webapp"
)

aboveten=[]

app = Flask(__name__)

@app.route("/")
def home():
    return "ok"

@app.route("/student")
def student():
    cursor = db.cursor()
    cursor.execute("select * from student")
    students=cursor.fetchall()
    for student in students:
        if student[3] >= 10:
            aboveten.append(student)
    return render_template("student.html", students=aboveten)

@app.route("/student/<id>")
def studentDetail(id):
    cursor=db.cursor()
    sql = "select firstname, exam_note from student where id = %s"
    params = (id, ) 
    cursor.execute(sql, params)
    firstname, note = cursor.fetchall()[0]
    resp = f"{firstname} a obtenu la note de: {note}/20"
    return resp

#Démarrage du serveur
app.run(host="0.0.0.0", port=8080)