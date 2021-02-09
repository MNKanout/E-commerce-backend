#Libraries to import
import time
import pymongo


main_menu = '''\nPlease choose one of the following options:\n
1.Login
2.Search
3.Quit
'''

login_menu = '''\nPlease select a customer account:\n
1.Login
2.Search
\n3.Quit
'''


order_menu = 
'''\nIn order to use order operations, you have to select a customer first:\n
1.Select a customer
2.Order operations
3.Quit
'''

search_menu = '''\nPlease choose one of the following options:\n
1.Show all customers
2.Show all products
3.Show all orders
4.Search for a customer
5.Search for a product
6.Search for an order
'''

#Interface
def main():
    print("Main Menu")
    while True:
        choice = input(menu)
        if choice == "1":
            return(print("You choose 1"))
            break

        elif choice == "2":
            return(print("You choose 2"))
            break

        elif choice == "3"

        else:
            return "You selected an invalid option, please select a valid option"
            continue

def Customer_menu():
    print("Customer Menu")
    while True:
        choice = input(menu)
        if choice == "1":
            return(print("You choose 1"))
            break

        elif choice == "2":
            return(print("You choose 2"))
            break

        else:
            return "You selected an invalid option, please select a valid option"
            continue










if __name__ == "__main__":
    main()