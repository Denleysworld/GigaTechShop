from .config import conn, cursor

class Customer:
    def __init__(self, name, email, phone, address, customer_id=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"<Customer {self.customer_id} {self.name}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Customer table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS customers;"
        cursor.execute(sql)
        conn.commit()
        print("Customer table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO customers (name, email, phone, address)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.email, self.phone, self.address))
        conn.commit()
        self.customer_id = cursor.lastrowid

    @classmethod
    def create(cls, name, email, phone, address):
        customer = cls(name, email, phone, address)
        customer.save()
        return customer

    @classmethod
    def find_by_id(cls, customer_id):
        sql = "SELECT * FROM customers WHERE customer_id = ?"
        cursor.execute(sql, (customer_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    def update(self, name, email, phone, address):
        sql = """
            UPDATE customers
            SET name = ?, email = ?, phone = ?, address = ?
            WHERE customer_id = ?
        """
        cursor.execute(sql, (name, email, phone, address, self.customer_id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM customers WHERE customer_id = ?"
        cursor.execute(sql, (self.customer_id,))
        conn.commit()
