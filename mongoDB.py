from pymongo import MongoClient
import json
from log import json_connector 


class MongoDB_saveto():
        
        def save_to(self , data_json):

            # Create connection to MongoDB
            client = MongoClient('localhost', 27017)
            db = client['ML_DB']
            collection = db['INPUT_DATA']

            # Build a basic dictionary  
            # d = {'website': 'www.carrefax.com', 'author': 'Daniel Hoadley', 'colour': 'purple'}

            # Insert the dictionary into Mongo
            collection.insert_one(data_json)
            # collection.insert(data_json)
            # URI ='mongodb://127.0.0.1:13022'
            
            # myclient = MongoClient("mongodb://localhost:27017/")  # URI OR THIS ONE

            # db = myclient["GFG"]
            # Collection = db["data"]

            # with open(data_json) as file:
            #     file_data = json.load(file)
                
            # if isinstance(file_data, list):
            #     Collection.insert_many(file_data)
            # else:
            #     Collection.insert_one(file_data)
