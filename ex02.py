from pymongo import MongoClient
from bson.json_util import dumps
import pprint
client = MongoClient('localhost', 27017)
myDB = client.bit
mycol = myDB.student

# pprint.pprint(mycol.find())

# for doc in mycol.find():
#     pprint.pprint(doc)

# for doc in mycol.find({"kor": {"$gte": 80}}, {"_id":0}):
#     pprint.pprint(doc)

arr = mycol.find({"kor": {"$gte": 80}}, {"_id":0})

r = dumps(arr, ensure_ascii=False)
print(r)