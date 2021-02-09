from flask import Flask, render_template, request, redirect, Blueprint
from models.bike import Bike
from models.manufacturer import Manufacturer
import repositories.bike_repository as bike_repository
import repositories.manufacturer_repository as manufacturer_repository


bikes_blueprint = Blueprint("/bikes", __name__)


@bikes_blueprint.route("/bikes")
def bikes():
    bikes = bike_repository.select_all()
    return render_template("bikes/index.html", all_bikes = bikes, title="Mikes Bikes - Bikes")

@bikes_blueprint.route("/bikes/all")
def bikes_all():
    bikes = bike_repository.select_all()
    return render_template("bikes/all.html", all_bikes = bikes, title="Mikes Bikes - All Stock")

@bikes_blueprint.route("/bikes/new", methods=['GET'])
def new_bike():
    manufacturers = manufacturer_repository.select_all()
    return render_template("bikes/new.html", all_manufacturers = manufacturers, title="Mikes Bikes - Create New Bike")

@bikes_blueprint.route("/bikes", methods=['POST'])
def create_bike():
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    model = request.form['model']
    description = request.form['description']
    buy_cost = request.form['buy_cost']
    sell_price = request.form['sell_price']
    stock_level = request.form['stock_level']
    bike = Bike(manufacturer, model, description, buy_cost, sell_price, stock_level)
    bike_repository.save(bike)
    return redirect('/bikes')

@bikes_blueprint.route("/bikes/<id>", methods=['GET'])
def show_bike(id):
    bike = bike_repository.select(id)
    # mark_up = (bike.buy_cost / bike.sell_price) * 100 
    return render_template('bikes/show.html', bike = bike, title="Mikes Bikes - Selected Bike")

@bikes_blueprint.route("/bikes/<id>/edit", methods=['GET'])
def edit_bike(id):
    bike = bike_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('bikes/edit.html', bike = bike, all_manufacturers = manufacturers, title="Mikes Bikes - Edit Bike")

@bikes_blueprint.route("/bikes/<id>", methods=['POST'])
def update_bike(id):
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    model = request.form['model']
    description = request.form['description']
    buy_cost = request.form['buy_cost']
    sell_price = request.form['sell_price']
    stock_level = request.form['stock_level']
    update_mark_up = round((((float(sell_price) - float(buy_cost)) / float(buy_cost)) * 100), 2) 
    bike = Bike(manufacturer, model, description, buy_cost, sell_price, stock_level, update_mark_up, id)
    bike_repository.update(bike)
    return redirect('/bikes')

@bikes_blueprint.route("/bikes/<id>/delete", methods=['POST'])
def delete_bike(id):
    bike_repository.delete(id)
    return redirect('/bikes')
