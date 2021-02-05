from flask import Flask, render_template, request, Blueprint

bikes_blueprint = Blueprint("/bikes", __name__)

@bikes_blueprint.route("/bikes")
def bikes():
    return render_template("bikes/index.html")

@bikes_blueprint.route("/bikes/show")
def show():
    return render_template("bikes/show.html")