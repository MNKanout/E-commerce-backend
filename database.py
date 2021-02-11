from pymongo import MongoClient

# Connecting to the database
client = MongoClient('localhost',27017)


#Creating the database
db = client['mongo_university']
customers = db['customers']
products = db['products']
orders = db['orders']
