from flask import Flask, render_template, request, redirect, Blueprint
from models.bike import Bike
from models.manufacturer import Manufacturer
import repositories.bike_repository as bike_repository
import repositories.manufacturer_repository as manufacturer_repository


bikes_blueprint = Blueprint("/bikes", __name__)


@bikes_blueprint.route("/bikes")
def bikes():
    bikes = bike_repository.select_all()
    return render_template("bikes/index.html", all_bikes = bikes)

@bikes_blueprint.route("/bikes/new", methods=['GET'])
def new_bike():
    manufacturers = manufacturer_repository.select_all()
    return render_template("bikes/new.html", all_manufacturers = manufacturers)

@bikes_blueprint.route("/bikes", methods=['POST'])
def create_bike():
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    model = request.form['model']
    description = request.form['description']
    buy_cost = request.form['buy_cost']
    sell_price = request.form['sell_price']
    bike = Bike(manufacturer, model, description, buy_cost, sell_price)
    bike_repository.save(bike)
    return redirect('/bikes')

@bikes_blueprint.route("/bikes/<id>", methods=['GET'])
def show_bike(id):
    bike = bike_repository.select(id)
    return render_template('bikes/show.html', bike = bike)

@bikes_blueprint.route("/bikes/show")
def show():
    return render_template("bikes/show.html")