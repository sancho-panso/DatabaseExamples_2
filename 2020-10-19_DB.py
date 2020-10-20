from database import DatabaseContextManager

def create_table_customer():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    Customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    Company_id INTEGER,
    FOREIGN KEY (Company_id) REFERENCES Companies(Company_id)))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

def alter_table_customer():
    query = """ALTER TABLE Customers
    ADD Company_id INTEGER"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    Company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count INTEGER)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

def create_company(company_name: str, qnt: int):
    query = f"""INSERT INTO Companies(company_name, employee_count) VALUES(?,?)"""
    parameters = [company_name, qnt]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")



def create_customer(first_name: str, last_name: str, age: int, company: str):
    query = f"""INSERT INTO Customers(first_name, last_name, age, Company_id) VALUES(?,?,?,?)"""
    parameters = [first_name, last_name, age, company]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_customer_first_name(old_name: str, new_name: str):
    query = """UPDATE Customers
                SET first_name = ?
                WHERE first_name = ?"""
    parameters = [new_name, old_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

def update_customer_on_id(first_name: str, last_name: str, age: int, Customer_id: int ):
    query = """UPDATE Customers
                SET first_name = ?, last_name = ?, age  = ?
                WHERE Customer_id = ?"""
    parameters = [first_name, last_name, age, Customer_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

def delete_customer(id: int):
    query = """DELETE FROM Customers
                WHERE Customer_id = ?"""
    parameters = [id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

def get_companies_customers():
    query = """SELECT * FROM Companies
                JOIN Customers
                    ON Customers.Company_id = Companies.Company_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


#create_table_customer()
#create_customer("Moony","Mouse", 17, 1)
#get_customers()
#delete_customer()
#update_customer_first_name("Mikkes","Mike")
#update_customer_on_id("Moony","Mouse",16,2)
#get_customers()

#create_table_companies()
#create_company("UAB Spurga", 25)
#create_company("MB RA-gelis", 5)
#get_companies()
#alter_table_customer()

get_companies_customers()
