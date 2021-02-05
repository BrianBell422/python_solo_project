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

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['location'], result['product_type'])
    return manufacturer


def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)