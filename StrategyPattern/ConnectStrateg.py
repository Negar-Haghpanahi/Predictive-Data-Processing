from requests import request
from inputclass import *
from abc import ABC, abstractmethod
from codecs import ignore_errors
import pymssql
import pandas as pd
import SingletoneConnection_type
import SingletoneConnection_MongoDB
from pymongo import MongoClient
import pymongo
class ConnectContext():
    
    def __init__(self) -> None:
        pass
    
    def connectDB(self , classrequest:RelationalDBRequest):
        obj = classrequest
        if obj is not None :
            return RelationDB(classrequest).ConnectDB()

    def connectMongo(self , classrequest : MongoDBRequest):
        obj = classrequest
        if obj is not  None:
            return NoRelation_Mongo(classrequest).ConnectMongoDB()


class connectStrategy(ABC):
    def __init__(self ,request) :
        self.request=request
    
    def ConnectDB(self):
        pass

    def ConnectMongoDB(self):
        pass

class RelationDB(connectStrategy):

    def ConnectDB(self):
        s= SingletoneConnection_type.singletone(self.request)
        conn=s.connect()
        cursor = conn.cursor(as_dict=True)
        str="SELECT * FROM "
        cursor.execute(str+self.request.tablename)
        df=pd.DataFrame()
        for row in cursor:
            df=df.append(row,ignore_index=True)
        #conn.close()
        return df 

class NoRelation_Mongo(connectStrategy):

    def ConnectMongoDB(self):
        # s=SingletoneConnection_type.singletone(self.request)
        s = SingletoneConnection_MongoDB.singletone(self.request)
        conn=s.connect()
        db = conn[self.request.mongodb_name]
        collection =db[self.request.collection_name]
        test = pd.DataFrame(list(collection.find()))
        return test

        #client.close()
        # print("Connection Successful") 
