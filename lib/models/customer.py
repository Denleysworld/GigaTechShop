# models/customer.py

from .config import conn, cursor

class Customer:
    def __init__(self, name, email, phone, address, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            address TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Customer table created successfully")

    def save(self):
        if self.id:
            sql = """
                UPDATE customers SET name=?, email=?, phone=?, address=?
                WHERE id=?
            """
            cursor.execute(sql, (self.name, self.email, self.phone, self.address, self.id))
        else:
            sql = """
                INSERT INTO customers (name, email, phone, address)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(sql, (self.name, self.email, self.phone, self.address))
            self.id = cursor.lastrowid
        conn.commit()

    @classmethod
    def create(cls, name, email, phone, address):
        customer = cls(name, email, phone, address)
        customer.save()
        return customer

    @classmethod
    def find_by_id(cls, customer_id):
        sql = "SELECT * FROM customers WHERE id = ?"
        cursor.execute(sql, (customer_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    def delete(self):
        if self.id is not None:
            sql = "DELETE FROM customers WHERE id=?"
            cursor.execute(sql, (self.id,))
            conn.commit()

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM customers WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        if row:
            return cls(*row)
        else:
            return None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        rows = cursor.fetchall()
        customers = []
        for row in rows:
            customer = cls(*row)
            customers.append(customer)
        return customers
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS customers"
        cursor.execute(sql)
        conn.commit()
        print("Customer table dropped successfully.")
