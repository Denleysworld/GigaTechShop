from .config import conn, cursor

class Customer:
    def __init__(self, name, email, phone, address, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"<Customer {self.name} {self.email}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            phone VARCHAR,
            address TEXT
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
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, email, phone, address):
        customer = cls(name, email, phone, address)
        customer.save()
        return customer

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM customers WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None
