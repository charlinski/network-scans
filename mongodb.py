import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["p-seminar"]
collection = db["hosts"]


def findByIp(ip):
    host = collection.find_one({"address": ip})
    return host

def insertIntoDB(dict):
    collection.insert_one(dict)

def findAll():
    hosts = collection.find()
    return hosts

def findWhere(query):
    hosts = collection.find(query)
    return hosts

def addDataToObject(identifierAttributeName, identifierAttributeValue, newData):
    query = {identifierAttributeName: identifierAttributeValue}
    newValue = {"$set": newData}
    collection.update_one(query, newValue)