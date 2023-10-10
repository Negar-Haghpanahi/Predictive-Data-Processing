from matplotlib.pyplot import cla
from InputType.inputtype import type_
import pandas as pd
from abc import ABC, abstractmethod

from inputclass import ReadRequest 


class ReadContext():
    def __init__(self) -> None:
        pass

    # def read(self , filepath = None , type = None):   # correct input
    def read (self , classrequest:ReadRequest):
        
        if classrequest.filepath  is not None:
            if classrequest.read_type ==type_.csv.value:
                return Readcsv(classrequest).read()
            else :
                return Readexcel(classrequest).read()  

class ReadStrategy(ABC):
    
    def __init__(self  , classrequest:ReadRequest):
        self.request= classrequest

    def read(self):
        pass

#concrete stratigies

class Readcsv(ReadStrategy):

    def read(self):
        df=pd.read_csv(self.request.filepath)
        print(df)
        return df              

class Readexcel(ReadStrategy):

    def read(self):
        df=pd.read_excel(self.request.filepath)
        return df              


# if __name__ != "__main__":
   
#     context = Context()
#     context.read(r"C:\Users\asus\Desktop\New folder\dataset\src\datasetcsv\finalcsv.csv", type_.csv )  
   

