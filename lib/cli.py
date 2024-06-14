from models.product import Product
from models.customer import Customer
from models.order import Order
from models.order_item import OrderItem
from helpers import exit_program
import datetime

def main():
    create_tables()
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            product_management()
        elif choice == "2":
            customer_management()
        elif choice == "3":
            order_management()
        else:
            print("Invalid choice")

def create_tables():
    Product.drop_table()
    Customer.drop_table()
    Order.drop_table()
    OrderItem.drop_table()

    Product.create_table()
    Customer.create_table()
    Order.create_table()
    OrderItem.create_table()

def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Manage products")
    print("2. Manage customers")
    print("3. Manage orders")

def product_management():
    while True:
        print("\nProduct Management")
        print("0. Go back to main menu")
        print("1. Add new product")
        print("2. Delete a product")
        print("3. Update a product")
        print("4. Search for a product")
        print("5. List all products")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            add_new_product()
        elif choice == "2":
            delete_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            search_product()
        elif choice == "5":
            list_products()
        else:
            print("Invalid choice")

def add_new_product():
    print("Enter product details:")
    name = input("Name: ")
    description = input("Description: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    
    product = Product.create(name=name, description=description, price=price, quantity=quantity)
    print(f"Product '{product.name}' created successfully with ID {product.id}")

def delete_product():
    product_id = int(input("Enter the Product ID to delete: "))
    product = Product.find_by_id(product_id)
    if product:
        product.delete()
        print(f"Product ID {product_id} deleted successfully.")
    else:
        print("Product not found.")

def update_product():
    product_id = int(input("Enter the Product ID to update: "))
    product = Product.find_by_id(product_id)
    if not product:
        print("Product not found.")
        return

    print("Leave blank to keep current value.")
    name = input(f"Name ({product.name}): ") or product.name
    description = input(f"Description ({product.description}): ") or product.description
    price = input(f"Price ({product.price}): ") or str(product.price)
    quantity = input(f"Quantity ({product.quantity}): ") or str(product.quantity)

    product.name = name
    product.description = description
    product.price = float(price)
    product.quantity = int(quantity)
    product.save()
    print(f"Product ID {product_id} updated successfully.")

def search_product():
    name = input("Enter the Product Name to search: ")
    products = Product.find_by_name(name)
    if products:
        for product in products:
            print_product(product)
    else:
        print("No products found with that name.")

def list_products():
    products = Product.select()
    if products:
        for product in products:
            print_product(product)
    else:
        print("No products found.")

def print_product(product):
    print(f"ID: {product.id}, Name: {product.name}, Description: {product.description}, Price: {product.price}, Quantity: {product.quantity}")

def customer_management():
    while True:
        print("\nCustomer Management")
        print("0. Go back to main menu")
        print("1. Add new customer")
        print("2. Delete a customer")
        print("3. Update a customer")
        print("4. Search for a customer")
        print("5. List all customers")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            add_new_customer()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            search_customer()
        elif choice == "5":
            list_customers()
        else:
            print("Invalid choice")

def add_new_customer():
    print("Enter customer details:")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")

    customer = Customer.create(name=name, email=email, phone=phone, address=address)
    print(f"Customer '{customer.name}' created successfully with ID {customer.id}")

def delete_customer():
    customer_id = int(input("Enter the Customer ID to delete: "))
    customer = Customer.find_by_id(customer_id)
    if customer:
        customer.delete()
        print(f"Customer ID {customer_id} deleted successfully.")
    else:
        print("Customer not found.")

def update_customer():
    customer_id = int(input("Enter the Customer ID to update: "))
    customer = Customer.find_by_id(customer_id)
    if not customer:
        print("Customer not found.")
        return

    print("Leave blank to keep current value.")
    name = input(f"Name ({customer.name}): ") or customer.name
    email = input(f"Email ({customer.email}): ") or customer.email
    phone = input(f"Phone ({customer.phone}): ") or customer.phone
    address = input(f"Address ({customer.address}): ") or customer.address

    customer.name = name
    customer.email = email
    customer.phone = phone
    customer.address = address
    customer.save()
    print(f"Customer ID {customer_id} updated successfully.")

def search_customer():
    email = input("Enter the Customer Email to search: ")
    customer = Customer.find_by_email(email)
    if customer:
        print_customer(customer)
    else:
        print("Customer not found.")

def list_customers():
    customers = Customer.select()
    if customers:
        for customer in customers:
            print_customer(customer)
    else:
        print("No customers found.")

def print_customer(customer):
    print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}, Address: {customer.address}")

def order_management():
    while True:
        print("\nOrder Management")
        print("0. Go back to main menu")
        print("1. Place a new order")
        print("2. Delete an order")
        print("3. Update an order")
        print("4. Search for an order")
        print("5. List all orders")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            place_order()
        elif choice == "2":
            delete_order()
        elif choice == "3":
            update_order()
        elif choice == "4":
            search_order()
        elif choice == "5":
            list_orders()
        else:
            print("Invalid choice")

def place_order():
    customer_id = int(input("Enter customer ID to place order: "))
    customer = Customer.find_by_id(customer_id)
    if not customer:
        print("Customer not found.")
        return

    print(f"Placing order for customer: {customer.name}")

    # Use current date and time for the order_date
    order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order = Order.create(customer_id=customer.id, order_date=order_date, status="Pending")

    while True:
        product_id = int(input("Enter Product ID to add to order (0 to finish): "))
        if product_id == 0:
            break
        quantity = int(input(f"Enter quantity for Product ID {product_id}: "))

        product = Product.find_by_id(product_id)
        if not product:
            print("Product not found.")
            continue

        OrderItem.create(order_id=order.id, product_id=product_id, quantity=quantity, price=product.price)
        print(f"Added {quantity} units of '{product.name}' to the order.")

    print(f"Order placed successfully with ID {order.id} for customer {customer.name}")

def delete_order():
    order_id = int(input("Enter the Order ID to delete: "))
    order = Order.find_by_id(order_id)
    if order:
        order.delete()
        print(f"Order ID {order_id} deleted successfully.")
    else:
        print("Order not found.")

def update_order():
    order_id = int(input("Enter the Order ID to update: "))
    order = Order.find_by_id(order_id)
    if not order:
        print("Order not found.")
        return

    print("Leave blank to keep current value.")
    status = input(f"Status ({order.status}): ") or order.status

    order.status = status
    order.save()
    print(f"Order ID {order.id}and {order.status} updated successfully.")

def search_order():
    customer_id = int(input("Enter the Customer ID to search for orders: "))
    orders = Order.find_by_customer_id(customer_id)
    if orders:
        for order in orders:
            print(f"ID: {order.id}, Customer ID: {order.customer_id}, Status: {order.status}")
    else:
        print("No orders found for that customer.")

def list_orders():
    orders = Order.select()
    if orders:
        for order in orders:
            print(f"ID: {order.id}, Customer ID: {order.customer_id}, Status: {order.status}")
    else:
        print("No orders found.")

if __name__ == "__main__":
    main()

