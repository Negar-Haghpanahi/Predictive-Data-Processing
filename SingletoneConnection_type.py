from concurrent.futures import process
from requests import request
from traitlets import Instance
from StrategyPattern.ConnectStrateg import *
from threading import Lock, Thread
import inputclass
from inputclass import RelationalDBRequest

class Metaclasssingletone(type):

    _lock: Lock = Lock()
    instances = {}
    def __call__(cls, *args, **kwds) :

        with cls._lock:
            if  cls.__name__.capitalize() not in cls.instances:                                 
                instance=super().__call__(*args, **kwds)
                cls.instances[cls.__name__.capitalize()] = instance

        return cls.instances[cls.__name__.capitalize()]

    
class singletone( metaclass=Metaclasssingletone):
    
    def __init__(self, request:RelationalDBRequest):
        self.conn= pymssql.connect(request.servername, request.login, request.password, request.dbname)

    def connect(self):
        return self.conn
    























 

# if __name__ == "__main__":
#     servername =input("servername is\n") 
#     login =input("login is\n")
#     password =input("password is\n")
#     dbname = input("dbname is\n")
#     tablename =input("tablename is\n")
#     obj0 = inputclass.RelationalDBRequest(servername , login , password , dbname , tablename)
    
#     s1 = singletone(obj0)
    # conn=s1.connect(obj0)
    # print(conn)
    # process1 = Thread(target=s1.connect(obj0))
    # process1.start()
    



    #DESKTOP-F7TB0BK\MSSQLSERVER_13', 'sa', '****', "Sample"