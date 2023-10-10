from __future__ import annotations
from cgitb import handler
from multiprocessing.spawn import prepare
from traceback import print_tb
from matplotlib.pyplot import connect
from log.json_connector import save_input 
from requests import request
from StrategyPattern.ReadFileStrategy import * 
from StrategyPattern.PreperStrategy import *
from StrategyPattern.ClusterStrategy import *
from StrategyPattern.ModelStrategy1 import *
from StrategyPattern.ConnectStrateg import *
from StrategyPattern.SaveStrategy  import *
from InputType.inputtype import context
import pandas as pd
from abc import ABC, abstractmethod
from typing import Any, Optional
import os

from inputclass import Request

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[classmethod]: 
        pass


class ChainRequest(Handler):

    _next_handler: Handler = None
    _context:HandleContext=None
    def __init__(self, context) -> None:
        self._context=context
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, df: pd.DataFrame=None) -> classmethod:
        df=self._context.execute(df)
        if self._next_handler:
            return self._next_handler.handle(df)
        return None

class HandleContext:
    def __init__(self, chain_type,request:Request) -> None:
        self.chain_type=chain_type
        self.request=request

    def execute(self,df):            
        self.request.df=df
        if self.chain_type == context.connect:
            connect_context = ConnectContext()    
            connect_obj = connect_context.connectDB(self.request)
            self.request.df = connect_obj
            save_json = save_input()
            save_json.Prepare_json()
            req = save_json.remove_df()
            
            return connect_obj

        elif self.chain_type == context.read:
            read_context =ReadContext()
            read_obj = read_context.read(self.request) 
            self.request.df=read_obj
            return read_obj                  
            

        elif self.chain_type == context.prepare:
            prep_context =PrepareContext()
            prep_obj=prep_context.prep(self.request) 
            self.request.df = prep_obj
            return prep_obj                          

        elif self.chain_type == context.cluster:
            cluster_context = Clustercontext()
            cluster_obj=cluster_context.executeCluster(self.request)
            self.request.df=cluster_obj
            return cluster_obj

        elif self.chain_type == context.model :
            model_context = ModelContext()                      
            model_obj =model_context.executeModel(self.request)           
            self.request.df =model_obj
            return model_obj
        
        else:
            save_context = Savecontext()
            save_obj = save_context.executesave(self.request)
            self.request.df = save_obj
            return save_obj
            # self.request.df =save_obj
            # return save_obj
            



# #def client_code(handler: Handler) -> None:
# if __name__ == "__main__":
#     #result = handler.handle(df)
#     cluster = ClusterHandler()
#     prep =PrepHandler()
#     model=ModelHandler()
#     cluster.set_next(prep).set_next(model)
#     cluster.handle(df)
    




