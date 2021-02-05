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

def delete_all():
    sql = "DELETE FROM bikes"
    run_sql(sql)