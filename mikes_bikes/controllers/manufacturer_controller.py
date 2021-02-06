from flask import Flask, render_template, request, redirect, Blueprint
from models.manufacturer import Manufacturer
import repositories.bike_repository as bike_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("/manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    return render_template("manufacturers/new.html")

@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form['name']
    location = request.form['location']
    product_type = request.form['product_type']
    manufacturer = Manufacturer(name, location, product_type)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

@manufacturers_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/show.html', manufacturer = manufacturer)

@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturers(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer = manufacturer)

@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    location = request.form['location']
    product_type = request.form['product_type']
    manufacturer = Manufacturer(name, location, product_type, id)
    manufacturer_repository.update(manufacturer)
    return redirect ('/manufacturers')

@manufacturers_blueprint.route("/manufacturers/show")
def show():
    return render_template("manufacturers/show.html")

@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')