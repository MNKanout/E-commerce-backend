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

(b) to go back"
'''

cart_m = '''
Cart Menu

1.Add product to cart
2.Remove product from cart
3.Show products in cart
4.Empty cart
5.Show products in store

(b) to go back"
'''


search_menu = '''\nPlease choose one of the following options:\n
1.Show all customers
2.Show all products
3.Show all orders
4.Search for a customer
5.Search for a product
6.Search for an order

(b) to go back"
'''

def get_customers(documents):
    for document in documents.find():
        print(int(document["customer_id"]), document["first_name"].title(),document["last_name"].title())



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

def customer_menu(customer_id):
    customer = customers.find_one({"customer_id":customer_id})
    while True:
        print("\nYou are logged in as " + customer['first_name'].title()
        ,customer['last_name'].title())
        print(customer_m)

        #Cart menu
        choice = input()
        if choice == "1":
            cart_menu(customer_id)

        #Show Orders
        elif choice == "2":
            pass

        elif choice == "3":
            pprint.pprint(customers.find_one({"customer_id":customer_id}))

        
        elif choice == "4":
            customers.find_one_and_delete({"customer_id":customer_id})
            break

        #Go back to the customer menu
        elif choice.lower() == "b":
            break

        # Invalid option
        else:
            print("You selected an invalid option, please select a valid option")


def cart_menu(customer_id):
    while True:
        print(cart_m)
        choice = input()

        #Add product to cart
        if choice == "1":
            product_id = input("Enter product number:\t")
            customers.update_one({"customer_id":customer_id},
            {
               "$push":{"cart":{"product_id":int(product_id),"Quantity":1}}
            })

        #Remove product from cart
        elif choice == "2":
            product_id = input("Enter the product number:\t")
            customers.update_one({"customer_id":customer_id},
            {
               "$pull":{"cart":{"product_id":int(product_id)}}
            })

        #Show products in cart
        elif choice == "3":
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
                {"$project":{"_id":0,"products.product_id":1,"products.product_name":1}},
            ])

            for item in cart_items:
                pprint.pprint(item)

        # Empty cart
        elif choice == "4":
             customers.update_one({"customer_id":customer_id},
            {
               "$set":{"cart":[]}
            })

        #Show products in store    
        elif choice == "5":
            print("\nAvailable products:")

            for product in products.find():
                print(int(product["product_id"]),product["product_name"],int(product["units_in_stock"]))
            
        #Go back to the customer menu
        elif choice.lower() == "b":
            break

        # Invalid option
        else:
            print("You selected an invalid option, please select a valid option")




        


    







if __name__ == "__main__":
    main()