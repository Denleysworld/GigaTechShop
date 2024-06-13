from models.customer import Customer
from models.product import Product
from models.category import Category
from models.order import Order
from models.order_item import OrderItem
from helpers import exit_program, helper_1

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            create_customer()
        elif choice == "3":
            create_product()
        elif choice == "4":
            list_customers()
        elif choice == "5":
            list_products()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Create a new customer")
    print("3. Create a new product")
    print("4. List all customers")
    print("5. List all products")


def create_customer():
    print("Enter customer details:")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")

    customer = Customer.create(name=name, email=email, phone=phone, address=address)
    print(f"Customer {customer.name} created successfully with ID {customer.id}")


def create_product():
    print("Enter product details:")
    name = input("Name: ")
    description = input("Description: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    category_id = int(input("Category ID: "))

    product = Product.create(name=name, description=description, price=price, quantity=quantity, category_id=category_id)
    print(f"Product {product.name} created successfully with ID {product.id}")


def list_customers():
    customers = Customer.select()
    if customers:
        print("List of Customers:")
        for customer in customers:
            print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}, Address: {customer.address}")
    else:
        print("No customers found")


def list_products():
    products = Product.select()
    if products:
        print("List of Products:")
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Description: {product.description}, Price: {product.price}, Quantity: {product.quantity}, Category ID: {product.category_id}")
    else:
        print("No products found")


if __name__ == "__main__":
    main()
