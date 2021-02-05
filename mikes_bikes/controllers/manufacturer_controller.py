from flask import Flask, render_template, request, Blueprint
from models.manufacturer import Manufacturer
import repositories.bike_repository as bike_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("/manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/show")
def show():
    return render_template("manufacturers/show.html")