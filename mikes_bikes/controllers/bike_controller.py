from flask import Flask, render_template, request, Blueprint
from models.bike import Bike
import repositories.bike_repository as bike_repository
import repositories.manufacturer_repository as manufacturer_repository


bikes_blueprint = Blueprint("/bikes", __name__)


@bikes_blueprint.route("/bikes")
def bikes():
    bikes = bike_repository.select_all()
    return render_template("bikes/index.html", all_bikes = bikes)

@bikes_blueprint.route("/bikes/show")
def show():
    return render_template("bikes/show.html")