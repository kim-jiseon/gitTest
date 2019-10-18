from pymongo import MongoClient
client = MongoClient('localhost', 27017)
myDB = client.bit
mycol = myDB.student
s = {"name":"김슬지", "kor":100, "eng":90, "math":80}
mycol.insert_one(s)
print(s)