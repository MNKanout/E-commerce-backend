#Libraries to import
import time
import pprint
from pymongo import MongoClient

host = MongoClient("localhost",27017)
db = host["e-commerce"]
customers = db["customers"]
products = db["products"]
orders = db["orders"]


main_m = '''
Welcome to the E-commerce demo app

Main Menu
Please log in as one of the following customers to continue:
'''

customer_m = '''
Customer Menu

1.Cart
2.Orders
3.Personal detials
4.Delete account

(q) to exit (b) to go back"
'''

cart_m = '''
Cart Menu

1.Search for a product
2.Show all products
3.Select a product
4.Remove a product
5.Show products in cart

(q) to exit (b) to go back"
'''


search_menu = '''\nPlease choose one of the following options:\n
1.Show all customers
2.Show all products
3.Show all orders
4.Search for a customer
5.Search for a product
6.Search for an order

(q) to exit (b) to go back"
'''

def get_customers(documents):
    for document in documents.find():
        print(str(document["customer_id"])+".", document["first_name"].title(),document["last_name"].title())



#Interface
def main():
    while True:
        print(main_m)
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
    while True:
        print(cart_m)
        choice = input()
        if choice == "1":
            pass

        #Show all products
        elif choice == "2":
            print("\nAvailable products:")
            for product in products.find():
                print(product["product_id"],product["product_name"])

        #Select a product
        elif choice == "3":
            product_id = input("Enter the product number:\t")
            customers.update_one({"customer_id":customer_id},
            {
               "$push":{"cart":{"product_id":product_id}
            })

        #Remove a product
        elif choice == "4":
            product_id = input("Enter the product number:\t")
            customers.update_one({"customer_id":customer_id},
            {
               "$pull":{"cart":{"product_id":product_id}}
            })

        elif choice == "5":
            cart_items = customers.aggregate([
                {
                    "$match":
                    {
                        "customer_id":customer_id
                    }
                },
                {
                    "$lookup":
                    {
                        "from":"products",
                        "localField":"cart.product_id",
                        "foreignField":"product_id",
                        "as": "products"
                    }
                },
                {"$project":{"_id":0,"products.product_name":1}},
            ])

            for item in cart_items:
                print(item)
            
        #Go back to the customer menu
        elif choice.lower() == "b":
            customer_menu(customer_id)

        #Quit the program
        elif choice.lower() == "q":
            break

        # Invalid option
        else:
            print("You selected an invalid option, please select a valid option")



def customer_menu(customer_id):
    customer = customers.find_one({"customer_id":customer_id})
    while True:
        print("\nYou are logged in as " + customer['first_name'].title()
        ,customer['last_name'].title())
        print(customer_m)

        #User choice
        choice = input()
        if choice == "1":
            products_menu(customer_id)

        #Go back to the customer menu
        elif choice.lower() == "b":
            main()

        #Quit the program
        elif choice.lower() == "q":
            break

        # Invalid option
        else:
            print("You selected an invalid option, please select a valid option")
        


    







if __name__ == "__main__":
    main()