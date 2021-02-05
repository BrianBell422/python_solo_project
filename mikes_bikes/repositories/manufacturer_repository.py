from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.bike import Bike

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, location, product_type) VALUES (%s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.location, manufacturer.product_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)