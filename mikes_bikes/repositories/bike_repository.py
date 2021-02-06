from db.run_sql import run_sql

from models.bike import Bike
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(bike):
    sql = "INSERT INTO bikes (manufacturer_id, model, description, buy_cost, sell_price) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [bike.manufacturer.id, bike.model, bike.description, bike.buy_cost, bike.sell_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    bike.id = id
    return bike

def select_all():
    bikes = []

    sql = "SELECT * FROM bikes"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        bike = Bike(manufacturer, row['model'], row['description'], row['buy_cost'], row['sell_price'], row['id'])
        bikes.append(bike)
    return bikes

def select(id):
    bike = None
    sql = "SELECT * FROM bikes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        bike = Bike(manufacturer, result['model'], result['description'], result['buy_cost'], result['sell_price'], result['id'])
    return bike

def delete_all():
    sql = "DELETE FROM bikes"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM bikes WHERE id = %s"
    values = [id]
    run_sql(sql, values)