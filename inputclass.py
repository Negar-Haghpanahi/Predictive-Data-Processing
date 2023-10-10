from tkinter.messagebox import NO
from requests import request


class Request():
    def __init__(self) -> None:
        self.df=None 
        self.target_col =None  
    
    def make_dict(self):
        for key in self.__dict__:                           
            yield (key ,'value {}'.format(key))  

class ReadRequest(Request):
    def __init__(self ) -> None:
        super().__init__()
        self.filepath = None
        self.read_type = None

class PrepRequest(Request):
    def __init__(self ) -> None:
        super().__init__()
        self.colname = None
        self.idxlist =None
        self.type_ =None
                      

class ClusterRequest(Request):
    def __init__(self)  -> None:
        super().__init__()
        self.clusterModel = None
        self.target_col = None
        self.categorical_features_idx = None
        self.numerical_idx = None
                  
        
class PridictModelRequest(Request):
    def __init__(self ) -> None:
        super().__init__()
        self.pridictModel =None
        self.target_col = None
        self.splitdata_catidx= None



class RelationalDBRequest (Request):
    def __init__(self) -> None:
        super().__init__()
        self.connect_type = None
        self.servername = None
        self.login = None
        self.password = None
        self.dbname = None
        self.tablename = None

class MongoDBRequest(Request):
    def __init__(self) -> None:
        super().__init__()
        self.connect_type = None
        self.URI = None
        self.client = None
        self.mongodb_name = None
        self.collection_name = None
        self.input_json = None


class PrepareCheck(Request):
    def __init__(self) -> None:
        super().__init__()
    
        self.dropcolumn = None
        self.model = None
        self.list = None
    

class SaveRequest(Request):
    def __init__(self) -> None:
        super().__init__()
        self.savemodel = None
        self.filepath = None
        self.servername = None
        self.login = None
        self.password = None
        self.dbname = None
        self.tablename = None
        self.ipaddress =None
        self.port = None
        self.client_Name = None
        self.collection_Name = None


class InputClass_json(Request):
    def __init__(self) -> None:
        super().__init__()
        self.read_request =None
        self.prepare_request = None
        self.cluster_request = None
        self.modelpridiction_request =None
        self.relationalDB_request =None
        self.prepareCheck_request =None
        self.save_request =None
        self.NoneRelation_Mongo = None

    # def make_dict(self):
    #     result={}
    #     result['read_request']    =(self.read_request.make_dict())
    #     result['prepare_request'] =(self.cluster_request.make_dict())
    #     result['cluster_request'] =(self.cluster_request.make_dict())
    #     result['modelpridiction_request'] =(self.modelpridiction_request.make_dict())
    #     result['relationalDB_request'] =(self.relationalDB_request.make_dict())
    #     result['prepareCheck_request'] =(self.prepareCheck_request.make_dict())
    #     result['saverequest_request'] = (self.saverequest_request.make_dict())
        # return result
