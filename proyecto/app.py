from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, ConnectionFailure
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "El_Panadero_Con_El_Pan"

usuarios = {
    "angel@gmail.com": "1234"
}

@app.route("/")
def inicio():
    return render_template("base.html")


@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    nombre = request.form.get("nombre")
    return render_template("formulario.html", nombre=nombre)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        contraseña = request.form["contraseña"]

        if correo in usuarios and usuarios[correo] == contraseña:
            flash("Bienvenido 😃")
            return redirect(url_for("inicio"))
        else:
            flash("Correo o contraseña incorrectos")
            return redirect(url_for("login"))

    return render_template("inicio_de_sesion.html")


@app.route("/recuperar", methods=["GET", "POST"])
def recuperar():
    if request.method == "POST":
        flash("Si el correo existe, se enviaron instrucciones")
        return redirect(url_for("login"))

    return render_template("recuperar_contraseña.html")


@app.route("/recetas")
def recetas():
    return "<h2>Recetas próximamente 👀</h2>"


@app.route("/educacion")
def educacion():
    return "<h2>Sección de educación 📚</h2>"


@app.route("/tmb")
def tmb():
    return "<h2>Calculadora TMB</h2>"


@app.route("/gct")
def gct():
    return "<h2>Calculadora GCT</h2>"


@app.route("/macros")
def macros():
    return "<h2>Calculadora de macros</h2>"


@app.route("/peso_ideal")
def peso_ideal():
    return "<h2>Peso ideal</h2>"


@app.route("/nutrientes")
def nutrientes():
    return "<h2>Información de nutrientes</h2>"


@app.route("/clear")
def clear():
    flash("Datos borrados")
    return redirect(url_for("formulario"))


if __name__ == "__main__":
    app.run(debug=True)