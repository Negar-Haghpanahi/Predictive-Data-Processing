import imp
import pandas as pd
from abc import ABC, abstractmethod
import inputclass
from inputclass import PrepareCheck
from InputType.inputtype import prepare_
 
class PrepareContext():

    def __init__(self) -> None:
        pass

    # def prep(self , dataframe = None):
    def prep(self , classrequest :PrepareCheck):
      
        if classrequest.df is not None and classrequest.model == prepare_.drop_column :
            drop_strategy = drop(classrequest)          
            return drop_strategy.execute() 
        elif classrequest.df is not None and classrequest.model == prepare_.change_type :
            change_strategy = changetype(classrequest)
            return change_strategy.execute()
        


class PrepStrategy(ABC):

    def __init__(self , classrequest :PrepareCheck):
        self.request = classrequest

    def execute(self):
        pass

class drop(PrepStrategy):

    def execute(self):
       
        self.request.df = self.request.df.dropna(axis = 0)   
        self.request.df = self.request.df.drop (self.request.dropcolumn , axis =1)

        return self.request.df
    
    
class changetype(PrepStrategy):

    def execute(self):
        list_col = self.request.df.columns

        for i in range(0 , len(self.request.list)):
            self.request.df[list_col[self.request.list[i]]] = self.request.df[list_col[self.request.list[i]]].astype(int)
        print(self.request.df.dtypes)            
        return self.request.df




# if __name__ != "__main__":
#     context = Context()
#     context.prep(df)

