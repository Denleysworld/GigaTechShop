from .config import conn, cursor

class Product:
    def __init__(self, name, description, price, quantity, product_id=None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"<Product {self.product_id} {self.name} {self.price}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            quantity INTEGER NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Product table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS products;"
        cursor.execute(sql)
        conn.commit()
        print("Product table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO products (name, description, price, quantity)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.description, self.price, self.quantity))
        conn.commit()
        self.product_id = cursor.lastrowid

    @classmethod
    def create(cls, name, description, price, quantity):
        product = cls(name, description, price, quantity)
        product.save()
        return product

    @classmethod
    def find_by_id(cls, product_id):
        sql = "SELECT * FROM products WHERE product_id = ?"
        cursor.execute(sql, (product_id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def select(cls):
        sql = "SELECT * FROM products"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    def update(self, name, description, price, quantity):
        sql = """
            UPDATE products
            SET name = ?, description = ?, price = ?, quantity = ?
            WHERE product_id = ?
        """
        cursor.execute(sql, (name, description, price, quantity, self.product_id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM products WHERE product_id = ?"
        cursor.execute(sql, (self.product_id,))
        conn.commit()
