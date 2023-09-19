CREATE TABLE items(
 item_id SERIAL PRIMARY KEY,
 item_name VARCHAR (50) NOT NULL,
 item_price FLOAT
);

CREATE TABLE customers(
 customer_id SERIAL PRIMARY KEY,
 customer_fname VARCHAR (50) NOT NULL,
 customer_lname VARCHAR (50) NOT NULL
);

INSERT INTO items (item_name, item_price)
VALUES
('Small Desk', 100), ('Large Desk', 300), ('Fan', 80);

-- Fetch all the items
SELECT * FROM items;

-- Fetch all the items with a price above 80 (80 not included)
SELECT * FROM items
WHERE item_price > 80;

-- All the items with a price below 300 (300 included)
SELECT * FROM items
WHERE item_price <= 300;


-- UPDATE items
-- SET item_name = 'Fan'
-- WHERE item_id = 3;

INSERT INTO customers (customer_fname, customer_lname)
VALUES
('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');

-- All customers whose last name is ‘Smith’ 
SELECT * FROM customers
WHERE customer_lname = 'Smith';

-- All customers whose last name is ‘Jones’
SELECT * FROM customers
WHERE customer_lname = 'Jones';

-- All customers whose firstname is not ‘Scott’
SELECT * FROM customers
WHERE customer_fname != 'Scott';