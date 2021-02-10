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

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['location'],row['product_type'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['location'], result['product_type'], result['id'] )
    return manufacturer

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, location, product_type) = (%s, %s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.location, manufacturer.product_type, manufacturer.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def bikes(manufacturer):
    bikes = []

    sql = "SELECT * FROM bikes WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        bike = Bike(row['manufacturer_id'], row['model'], row['description'], row['buy_cost'], row['sell_price'], row['stock_level'], row['mark_up'], row['id'])
        bikes.append(bike)
    return bikes