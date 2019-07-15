
import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://thanhnp:FEiM0OT3GTVUuhgO@cluster0-cqmi3.mongodb.net/test?retryWrites=true&w=majority")

db = client.mindx
def insert(name,age):
    db.hocvien.insert.one({'name':name, 'age':age})
insert('hoa':90)

# db.use.insert_one({"name":"hoa",'age':30})
# db.use.insert_one({"name":"lan",'age':30})
# db.use.insert_one({"name":"long",'age':30})
# db.use.insert_one({"name":"hoa",'age':31})

db.use.update_one({'name':'lan'}, {'$set':{'age':40}})
# print (list(db.use.find({'name':'hoa','age':31})))
# for v in db.use.find()
#     print(v)