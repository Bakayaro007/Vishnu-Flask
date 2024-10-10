import sqlite3
conn = sqlite3.connect('customers_items.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL);''')
cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL);''')
cursor.executemany('''
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'vision pro'),
    (2, 'computer'),
    (3, 'speaker'),
    (4, 'charger')
])
cursor.execute("Select *from products")
print("\n Products Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
cursor.executemany('''
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'John Doe'),
    (2, 'Jane Smith'),
    (3, 'Alice Johnson'),
    (4, 'Bob Brown')
])
cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
cursor.execute('''
    SELECT products.product_name, customers.customer_name
    FROM products
    CROSS JOIN customers;
''')
print("Cross Join \n")
rows = cursor.fetchall()
print("Product Name  | Customer Name")
print("-----------------------------")
for row in rows:
    product_name = row[0]
    customer_name = row[1]
    print(f"{product_name:<12} | {customer_name}")

conn.commit()
conn.close()