

from .config import conn, cursor

class Product:
    def __init__(self, name, description, price, quantity, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"<Product {self.name}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
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
        if self.id is None:
            sql = """
                INSERT INTO products (name, description, price, quantity)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(sql, (self.name, self.description, self.price, self.quantity))
            self.id = cursor.lastrowid
        else:
            sql = """
                UPDATE products
                SET name = ?, description = ?, price = ?, quantity = ?
                WHERE id = ?
            """
            cursor.execute(sql, (self.name, self.description, self.price, self.quantity, self.id))
        conn.commit()

    @classmethod
    def create(cls, name, description, price, quantity):
        product = cls(name=name, description=description, price=price, quantity=quantity)
        product.save()
        return product

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM products WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM products WHERE name LIKE ?"
        cursor.execute(sql, ('%' + name + '%',))
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def select(cls):
        sql = "SELECT * FROM products"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    def delete(self):
        sql = "DELETE FROM products WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()
        print(f"Product ID {self.id} deleted successfully.")
