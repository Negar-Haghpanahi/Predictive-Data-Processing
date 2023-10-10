from inputclass import SaveRequest
from InputType.inputtype import Save_file
from abc import ABC, abstractmethod
from pathlib import Path
from sqlalchemy import create_engine
import pandas as pd
import mongoDB
from pymongo import MongoClient
import json
from log import json_connector 
import SingletoneConnection_MongoDB


class Savecontext():

    def __init__(self) -> None:
        pass

    def executesave(self, classrequest:SaveRequest):
        if classrequest.savemodel ==Save_file.save_to_csv.value:
            save_csv =Save_To_CSV(classrequest)
            return save_csv.execute()            #no returnnnnn

        elif classrequest.savemodel == Save_file.save_to_excel.value:
            save_excel = Save_To_excel(classrequest)
            return save_excel.execute()
            #no returnnnnn
        elif classrequest.savemodel == Save_file.save_to_db:
            save_DB = Save_To_DB(classrequest)
            return save_DB.execute()
        else:
            save_mongo =Save_To_Mongo(classrequest)
            return save_mongo.execute()




class SaveStrategy(ABC):

    def __init__(self ,classrequest ) -> None:
        self.request = classrequest
        
    def execute(self):
        pass

class Save_To_CSV(SaveStrategy):

    def execute(self):
        filepath = Path(self.request.filepath)
        filepath.parent.mkdir(parents=True , exist_ok=True)
        self.request.df.to_csv(filepath)
        return self.request.df
        


class Save_To_excel(SaveStrategy):

    def execute(self):
        filepath =self.request.filepath
        writer = pd.ExcelWriter(filepath)
        self.request.df.to_excel(writer)
        writer.save()
        return self.request.df
        

class Save_To_DB(SaveStrategy):

    def execute(self):
    
        postgres_str = f'postgresql://{self.request.login}:{self.request.password}@{self.request.ipaddress}:{self.request.port}/{self.request.dbname}'
        cnx = create_engine(postgres_str)
        self.request.df.to_sql(self.request.tablename, con=cnx, index=False)
        return self.request.df


class Save_To_Mongo(SaveStrategy):           
    def execute(self):

        s = SingletoneConnection_MongoDB.singletone(self.request)
        conn_singletone = s.connect()
        db = conn_singletone[self.request.client_Name]
        collection = db[self.request.collection_Name]
        collection.insert_one(self.request.input_json)      
                                   #/////////////////
        return self.request.df




