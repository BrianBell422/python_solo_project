DROP TABLE manufacturers;
DROP TABLE bikes:

CREATE TABLE bikes (
    id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES manufacturers(id),
    model VARCHAR(255),
    description VARCHAR(255),
    buy_cost INT,
    sell_price INT
);

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    product_type VARCHAR(255)
);