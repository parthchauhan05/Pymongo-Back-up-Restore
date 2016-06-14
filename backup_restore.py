from os.path import join
import pymongo
from bson.json_util import dumps
# from bson.json_util import load
import json

def slice(sourcedict, string):
    for key in sourcedict.keys():
        if key.startswith(string) and key.endswith(string):
            del sourcedict[key]
    return sourcedict    

def backup_db(backup_db_dir):
    client = pymongo.MongoClient()
    database = client.test_db
    # authenticated = database.authenticate(<uname>,<pwd>)
    # assert authenticated, "Could not authenticate to database!"
    collections = database.collection_names()
    for i, collection_name in enumerate(collections):
        col = getattr(database,collections[i])
        collection = col.find()
        jsonpath = collection_name + ".json"
        jsonpath = join(backup_db_dir, jsonpath)
        with open(jsonpath, 'wb') as jsonfile:
            jsonfile.write(dumps(collection))

def restore_db(backup_file):
    client = pymongo.MongoClient()
    database = client.Retrive
    retrived = database['retrived']
    with open(backup_file,'r') as file:
        data = json.loads(file.read())
        for i in range(len(data)):
            '''
            Ingoring Random _id which contains special charactors which are not supported to insert in database
            If you have manually added your _id field then ignore slicing
            '''
            x = slice(data[i],"_id") 
            post_id = retrived.insert(data[i])