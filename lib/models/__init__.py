from models.customer import Customer
from models.product import Product
from models.order import Order
from models.order_item import OrderItem

# Drop existing tables if they exist
Customer.drop_table()
Product.drop_table()
Order.drop_table()
OrderItem.drop_table()

# Create tables
Customer.create_table()
Product.create_table()
Order.create_table()
OrderItem.create_table()

print("Tables created successfully.")
