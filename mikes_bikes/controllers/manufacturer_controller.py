from flask import Flask, render_template, request, Blueprint

manufacturers_blueprint = Blueprint("/manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    return render_template("manufacturers/index.html")

@manufacturers_blueprint.route("/manufacturers/show")
def show():
    return render_template("manufacturers/show.html")