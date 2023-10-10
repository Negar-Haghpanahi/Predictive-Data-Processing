from concurrent.futures import process
from requests import request
from traitlets import Instance
from StrategyPattern.ConnectStrateg import *
from threading import Lock, Thread
from inputclass import MongoDBRequest

class Metaclasssingletone(type):

    _lock: Lock = Lock()
    instances = {}
    def __call__(cls, *args, **kwds) :

        with cls._lock:
            if  cls.__name__.capitalize() not in cls.instances:                                 
                instance=super().__call__(*args, **kwds)
                cls.instances[cls.__name__.capitalize()] = instance

        return cls.instances[cls.__name__.capitalize()]

    
class singletone(metaclass=Metaclasssingletone):
    
    def __init__(self, request:MongoDBRequest):        # add request!!!!!!!!!!!!!

        self.conn=MongoClient('localhost', 27017)

    def connect(self):
        return self.conn
    

