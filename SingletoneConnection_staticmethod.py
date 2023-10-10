from __future__ import annotations
from abc import ABCMeta, abstractmethod
from concurrent.futures import process
from venv import create
from requests import request
from traitlets import Instance
from StrategyPattern.ConnectStrateg import *
from threading import Lock, Thread
import inputclass
from inputclass import RelationalDBRequest
from InputType import inputtype

class MetaclassSingletone(ABC):

    conn=None
    @staticmethod
    def connect(request):      #???????????
       pass

class singletone(MetaclassSingletone):

    conn=None
    @staticmethod
    def connect(request):
        if singletone.conn==None:
                singletone.conn= pymssql.connect(request.servername, request.login, request.password, request.dbname)
        return singletone.conn 
        























# if __name__ =="__main__":

#     conn = singletone.connect()
#     conn2 = singletone.connect()
#     #conn = S.connect()
