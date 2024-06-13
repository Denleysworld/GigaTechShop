from .config import conn, cursor

class Category:
    def __init__(self, name, description, id=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Category {self.name}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            description TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Category table created successfully")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS categories;"
        cursor.execute(sql)
        conn.commit()
        print("Category table dropped successfully")

    def save(self):
        sql = """
            INSERT INTO categories (name, description)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.description))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, description):
        category = cls(name, description)
        category.save()
        return category

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM categories WHERE id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        return cls(*row) if row else None
