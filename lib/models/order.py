from .config import conn, cursor

class Order:
    def __init__(self, customer_id, order_date, status, id=None):
        self.id = id
        self.customer_id = customer_id
        self.order_date = order_date
        self.status = status

    def __repr__(self):
        return f"<Order {self.id} {self.order_date} {self.status}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date DATETIME NOT NULL,
            status VARCHAR NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Order table created successfully")


    def save(self):
        sql = """
            INSERT INTO orders (customer_id, order_date, status)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.customer_id, self.order_date, self.status))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, customer_id, order_date, status):
        order = cls(customer_id, order_date, status)
        order.save()
        return order

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM orders WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM orders"
        cursor.execute(sql)
        rows = cursor.fetchall()
        orders = [cls(*row) for row in rows]
        return orders
