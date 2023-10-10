from __future__ import annotations
from cgitb import handler
from multiprocessing.spawn import prepare
from traceback import print_tb
import ReadingFile
import clustering
import Model
import pandas as pd
from abc import ABC, abstractmethod
from typing import Any, Optional


df = pd.read_csv(r"C:\Users\asus\Desktop\New folder\dataset\House_Rent_Dataset5.csv")
df=df.dropna(axis = 0)
df=df.drop('Posted On' , axis =1)
y= df.Rent

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[pd.DataFrame]:
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> pd.DataFrame:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class ClusterHandler(AbstractHandler):

    def handle(self, request: Any) -> pd.DataFrame:
        categorical_idx = [2,  3 , 4 , 5 , 6 , 7 ,9]  
        # if object.type == inputtype.type_.csv:
        object_cluster = clustering.Cluster(df , categorical_idx ,'Rent' ,y)
        #return df#object_cluster.df
        super().handle(object_cluster.df)
        #    return 

    
class PrepHandler(AbstractHandler):
    def handle(self, request: Any) -> pd.DataFrame:
        df0=request 
        object_prep = ReadingFile.Preparation(df0)
        object_prep.dropColumns(df0 , 'Floor')
        object_prep.dropColumns(df0 , 'Area Type')
        object_prep.dropColumns(df0 , 'Area Locality')
        object_prep.dropColumns(df0 , 'City')
        object_prep.dropColumns(df0 , 'Furnishing Status')
        object_prep.dropColumns(df0, 'Tenant Preferred')
        object_prep.dropColumns(df0 , 'Point of Contact')
        df=object_prep.dataframe
        # print(df)
        super().handle(df)

class ModelHandler(AbstractHandler):
    def handle(self, request: Any) -> pd.DataFrame:
        df=request
        Feature_Names =['BHK', 'Size', 'Bathroom', 'PostedOn', 'SuperArea',
        'CarpetArea', 'BuiltArea', 'Month', 'Day' ,'Rent','cluster','cluster_0' ,'cluster_1' ,'cluster_2']
        object_Model =Model.Models(df , Feature_Names)
        print(object_Model.df)
        return super().handle(object_Model.df)


#def client_code(handler: Handler) -> None:
if __name__ == "__main__":
    #result = handler.handle(df)
    cluster = ClusterHandler()
    prep =PrepHandler()
    model=ModelHandler()
    cluster.set_next(prep).set_next(model)
    cluster.handle(df)

    # prep.set_next(model)
    




