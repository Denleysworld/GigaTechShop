from .config import conn, cursor

class Order:
    def __init__(self, customer_id, order_date, status, order_id=None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.status = status

    def __repr__(self):
        return f"<Order {self.order_id} {self.order_date} {self.status}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date DATETIME NOT NULL,
            status VARCHAR NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Order table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS orders;"
        cursor.execute(sql)
        conn.commit()
        print("Order table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO orders (customer_id, order_date, status)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.customer_id, self.order_date, self.status))
        conn.commit()
        self.order_id = cursor.lastrowid

    @classmethod
    def create(cls, customer_id, order_date, status):
        order = cls(customer_id, order_date, status)
        order.save()
        return order

    @classmethod
    def find_by_id(cls, order_id):
        sql = "SELECT * FROM orders WHERE order_id = ?"
        cursor.execute(sql, (order_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM orders"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_customer_id(cls, customer_id):
        sql = "SELECT * FROM orders WHERE customer_id = ?"
        cursor.execute(sql, (customer_id,))
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    def update(self, customer_id, order_date, status):
        sql = """
            UPDATE orders
            SET customer_id = ?, order_date = ?, status = ?
            WHERE order_id = ?
        """
        cursor.execute(sql, (customer_id, order_date, status, self.order_id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM orders WHERE order_id = ?"
        cursor.execute(sql, (self.order_id,))
        conn.commit()
