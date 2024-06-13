from .config import conn, cursor

class Product:
    def __init__(self, name, description, price, quantity, category_id, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.category_id = category_id

    def __repr__(self):
        return f"<Product {self.name} {self.price}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            description TEXT,
            price DECIMAL(10, 2) NOT NULL,
            quantity INTEGER NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
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
            INSERT INTO products (name, description, price, quantity, category_id)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.description, self.price, self.quantity, self.category_id))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, description, price, quantity, category_id):
        product = cls(name, description, price, quantity, category_id)
        product.save()
        return product

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM products WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None
