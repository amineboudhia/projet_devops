import os
import subprocess
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import pymysql
import sys
from insert_values import inserto, get_data


#template_dir = os.path.abspath('templates')

app = Flask(__name__,template_folder="/home/devops/flask/flask/templates")


@app.route("/")
def hello_world():
    data=get_data()

    return render_template('index.html', data=data)


@app.route("/ajout",methods=["POST","GET"])
def Ajout():
    if request.method == "POST":
        name = request.form["nom"]
        prenom = request.form["prenom"]
        age = request.form["age"]
        inserto_new=inserto(name,prenom,age)

        return redirect(url_for('hello_world'))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
