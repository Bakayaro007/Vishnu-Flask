import sqlite3
conn = sqlite3.connect('joinmultiple.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        order_date TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    );
''')

cursor.executemany('''
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'Bruce'),
    (2, 'Tony Stark'),
    (3, 'Michael')
])

cursor.execute("Select *from customers")
print("\n Customers Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.executemany('''
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Speakerbar'),
    (2, 'Visionpro'),
    (3, 'ipad'),
    (4, 'computer')
])

cursor.execute("Select *from products")
print("\n Products Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, product_id, order_date) 
    VALUES (?, ?, ?, ?);
''', [
    (101, 1, 1, '2019-01-23'),  
    (102, 1, 2, '2021-01-17'), 
    (103, 2, 3, '2018-02-14'), 
    (104, 3, 4, '2022-02-09'), 
])

cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT customers.customer_name, products.product_name, orders.order_date
    FROM orders
    JOIN customers ON orders.customer_id = customers.customer_id
    JOIN products ON orders.product_id = products.product_id;
''')

rows = cursor.fetchall()

print("Customer Name  | Product Name  | Order Date")
print("-------------------------------------------")
for row in rows:
    customer_name = row[0]
    product_name = row[1]
    order_date = row[2]
    print(f"{customer_name:<14} | {product_name:<12} | {order_date}")

conn.commit()
conn.close()