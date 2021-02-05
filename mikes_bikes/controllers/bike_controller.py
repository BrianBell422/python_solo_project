from flask import Flask, render_template, request, Blueprint

bikes_blueprint = Blueprint("/bikes", __name__)

@bikes_blueprint.route("/bikes")
def bikes():
    return render_template("bikes/index.html")