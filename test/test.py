import json
from pprint import pprint

from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://joker787:Zxasqw1234@cluster0.gfdv3xl.mongodb.net/?retryWrites=true&w=majority"
# uri = 'mongodb+srv://db_telebot_user:XUK4QJdCJ9XfhiTG@atlascluster.k0w5qhu.mongodb.net/ProverkaAvto_RuBot'
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

my_db = client['test']
my_collection = my_db['food']
x = my_collection.find_one(name=1)
print(x)
# for x in my_collection.find({}, {'user_id': 1}):
#     print(x)
# my_collection.insert_one({
#     'user_id': 2,
#     'user_name': 'vika',
#     'mail': 'mail2@mail.ru'
# })

# for i in my_cursor:
#     print(i)

# print(my_db.list_collection_names())


# d = dict((db, [collection for collection in client[db].list_collections()])
#              for db in client.list_database_names())
# pprint(d)

# my_cursor = my_collection.find()
# for item in my_cursor:
#     print(item)




# my_db = client.test

# my_collection = my_db.foods

# my_collection.insert_one({
#     "name": "pizza",
#     "cal": 266,
#     "fats": {
#         "saturated": 4.5,
#         "trans": 0.2
#     },
#     "protein": 11
# })







# ['AUTO_checkBot',
# 'AUTO_informBot',
# 'AUTO_information_Bot',
# 'AVinformBot',
# 'Auto_CheckerBot',
# 'CarscanPro_Bot',
# 'ProverkaAvto_RuBot',
# 'newBot',
# 'admin',
# 'local']

