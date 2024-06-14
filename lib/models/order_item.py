from .config import conn, cursor

class OrderItem:
    def __init__(self, order_id, product_id, quantity, price, order_item_id=None):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"<OrderItem {self.order_id} {self.product_id} {self.quantity}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("OrderItem table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS order_items;"
        cursor.execute(sql)
        conn.commit()
        print("OrderItem table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO order_items (order_id, product_id, quantity, price)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.order_id, self.product_id, self.quantity, self.price))
        conn.commit()
        self.order_item_id = cursor.lastrowid

    @classmethod
    def create(cls, order_id, product_id, quantity, price):
        order_item = cls(order_id, product_id, quantity, price)
        order_item.save()
        return order_item

    @classmethod
    def find_by_id(cls, order_item_id):
        sql = "SELECT * FROM order_items WHERE order_item_id = ?"
        cursor.execute(sql, (order_item_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM order_items"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    def update(self, order_id, product_id, quantity, price):
        sql = """
            UPDATE order_items
            SET order_id = ?, product_id = ?, quantity = ?, price = ?
            WHERE order_item_id = ?
        """
        cursor.execute(sql, (order_id, product_id, quantity, price, self.order_item_id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM order_items WHERE order_item_id = ?"
        cursor.execute(sql, (self.order_item_id,))
        conn.commit()
