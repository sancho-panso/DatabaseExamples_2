from database import DatabaseContextManager



def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    Customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    amount_spent INTEGER)"""
    with DatabaseContextManager("order") as db:
        db.execute(query)

def create_table_products():
    query = """CREATE TABLE IF NOT EXISTS Products(
    Product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    price INTEGER,
    description TEXT)"""
    with DatabaseContextManager("order") as db:
        db.execute(query)

def create_table_orders():
    query = """CREATE TABLE IF NOT EXISTS Orders(
    Customer_id INTEGER,
    Product_id INTEGER)"""
    with DatabaseContextManager("order") as db:
        db.execute(query)

def create_product(product_name: str, price: int, desc: str):
    query = f"""INSERT INTO Products(product_name, price, description) VALUES(?,?,?)"""
    parameters = [product_name, price,  desc]
    with DatabaseContextManager("order") as db:
        db.execute(query, parameters)

def create_customer(first_name: str, last_name: str, amount: int):
    query = f"""INSERT INTO Customers(first_name, last_name, amount_spent) VALUES(?,?,?)"""
    parameters = [first_name, last_name, amount]
    with DatabaseContextManager("order") as db:
        db.execute(query, parameters)

def create_order(custom_id: int, product_id: int):
    query = f"""INSERT INTO Orders(Customer_id, Product_id) VALUES(?,?)"""
    parameters = [custom_id, product_id]
    with DatabaseContextManager("order") as db:
        db.execute(query, parameters)



def get_products():
    query = """SELECT * FROM Products"""
    with DatabaseContextManager("order") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")

def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("order") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")

def get_orders():
    query = """SELECT * FROM Orders"""
    with DatabaseContextManager("order") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_customer_on_id(first_name: str, last_name: str, amount: int, custom_id: int):
    query = """UPDATE Customers
                SET first_name = ?, last_name = ?, amount_spent  = ?
                WHERE Customer_id = ?"""
    parameters = [first_name, last_name, amount, custom_id]
    with DatabaseContextManager("order") as db:
        db.execute(query, parameters)


def update_product_on_id(product_name: str, price: int, desc: str, product_id: int ):
    query = """UPDATE Products
                SET product_name = ?, price = ?, desc  = ?
                WHERE Product_id = ?"""
    parameters = [product_name, price, desc, product_id]
    with DatabaseContextManager("order") as db:
        db.execute(query, parameters)

def update_order_on_id(custom_id: int, product_id: int, order_id: int ):
    query = """UPDATE Products
                SET Customer_id = ?, Product_id = ?
                WHERE Order_id = ?"""
    parameters = [custom_id, product_id, order_id]
    with DatabaseContextManager("order") as db:
        db.execute(query, parameters)

def delete_customer(id: int):
    query = """DELETE FROM Customers
                WHERE Customer_id = ?"""
    parameters = [id]
    with DatabaseContextManager("order") as db:
        db.execute(query, parameters)

def delete_product(id: int):
    query = """DELETE FROM Products
                WHERE Product_id = ?"""
    parameters = [id]
    with DatabaseContextManager("order") as db:
        db.execute(query, parameters)

def delete_order(id: int):
    query = """DELETE FROM Orders
                WHERE Product_id = ?"""
    parameters = [id]
    with DatabaseContextManager("order") as db:
        db.execute(query, parameters)



def get_companies_customers():
    query = """SELECT * FROM Companies
                JOIN Customers
                    ON Customers.Company_id = Companies.Company_id"""
    with DatabaseContextManager("order") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)

def get_productsBy_customers():
    query = """SELECT * FROM Orders
                JOIN Customers
                    ON Orders.Customer_id = Customers.Customer_id
                JOIN Products
                    ON Orders.Product_id = Products.Product_id"""
    with DatabaseContextManager("order") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)

#create_table_customers()
#create_customer("Miki","Mouse", 200)
#create_customer("Moony","Mouse", 150)
get_customers()

#create_table_products()
#create_product("Alice in WonderLand", 6.99, "book")
#create_product("Python for Dummies", 4.99, "book")
#create_product("How to learn French in two weeks", 16.99, "book")
#create_product("Fancy cooking", 8.00, "book")
get_products()

#create_table_orders()
#create_order(2,4)
#create_order(2,3)
#create_order(2,1)
#create_order(1,2)
get_orders()

get_productsBy_customers()
