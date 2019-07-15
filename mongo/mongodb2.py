import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb+srv://thanhnp:FEiM0OT3GTVUuhgO@cluster0-cqmi3.mongodb.net/test?retryWrites=true&w=majority"
    )

db = client.restaurant

def get_all_food():
    return list(db.foods.find())

def insert_food(name,price):
    db.foods.insert_one({'name':name,'price':price})

def delete_food_id(food_id):
    db.foods.delete_one({'_id':ObjectId(food_id)})

db.foods.insert_one({'name': 'ga ran', 'price': 160})
db.foods.insert_one({'name': 'com rang', 'price':30})