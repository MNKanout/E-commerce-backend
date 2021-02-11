#Libraries to import
import time
import pprint
from pymongo import MongoClient

host = MongoClient("localhost",27017)
db = host["e-commerce"]
customers = db["customers"]
products = db["products"]
orders = db["orders"]


cust_menu = '''
1.Add product to cart
2.Remove product from cart
2.Show products in cart
3.Checkout
4.Order history
5.Delete account

(b) to go main menu
'''


search_menu = '''\nPlease choose one of the following options:\n
1.Show all customers
2.Show all products
3.Show all orders
4.Search for a customer
5.Search for a product
6.Search for an order
'''

def get_customers(documents):
    for document in documents.find():
        print(str(document["customer_id"])+".", document["first_name"].title(),document["last_name"].title())



#Interface
def main():
    print("Welcome to the E-commerce demo app")
    while True:
        print("\nMain Menu\nPlease log in as one of the following customers to continue:")
        get_customers(customers)
        print("\n(q) to exit")
        choice = input()
        if choice == "1":
            customer_id = 1
            customer_menu(customer_id)
            
        elif choice == "2":
            customer_id = 2
            customer_menu(customer_id)

        elif choice == "3":
            customer_id = 3
            customer_menu(customer_id)

        elif choice.lower() == "q":
            print("Thanks for using the app!")
            break

        else:
            print("You selected an invalid option, please select a valid option")

def products_menu(customer_id):
    print("Products Menu")
    while True:
        print("\n1.Search for a product\n2.Show all products\n3.Select a product\n4.")
        choice = input()
        if choice == "1":
            pass
        elif choice == "2":
            for product in products.find():
                print(product["product_id"],product["product_name"])
        elif choice == "3":
            product_id = input("Enter the product number:\t")
            customers.update_one({"customer_id":customer_id},
            {
               "$push":{"cart":{"product_id":product_id}}
            })



def customer_menu(customer_id):
    print("Customer Menu")
    customer = customers.find_one({"customer_id":customer_id})
    while True:
        print("\nYou are logged in as " + customer['first_name'].title()
        ,customer['last_name'].title())
        print(cust_menu)
        choice_2 = input()
        if choice_2 == "1":
            products_menu(customer_id)
        elif choice_2.lower() == "b":
            customer_id = None
            main()
        else:
             print("You selected an invalid option, please select a valid option")
        


    







if __name__ == "__main__":
    main()