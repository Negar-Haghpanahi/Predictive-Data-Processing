from inputclass import SaveRequest

class Save_Builder():

    def __init__(self) -> None:
        
        self.file_path=''
        self.type_save=''
        self.serverName=''
        self.dbname=''
        self.login=''
        self.Password=''
        self.tablename=''
        self.ipadd=''
        self.port=''
        self.client_name = ''
        self.collection_name=''
        self.request =None


    def set_path(self , path):
        self.file_path = path
        return self
    
    def set_type(self, type_):
        self.type_save = type_
        return self

    def setServerName(self,serverName):
        self.serverName=serverName
        return self

    def setLogin(self,login):
        self.login=login
        return self

    def setPassword(self,password):
        self.Password=password
        return self

    def setDbname(self , dbname ):
        self.dbname=dbname
        return self

    def setTablename(self , tablename):
        self.tablename = tablename
        return self
    
    def setIPaddress(self, ipadd):
        self.ipadd = ipadd
        return self
    
    def setPort(self, port):
        self.port = port
        return self

    def setClient_Name(self, client):
        self.client_name = client
        return self

    def setCollection_Name(self , collection):
        self.collection_name = collection
        return self

    def create(self):
        save_obj=SaveRequest()
        save_obj.filepath  =self.file_path
        save_obj.savemodel =self.type_save
        save_obj.dbname = self.dbname
        save_obj.ipaddress =self.ipadd
        save_obj.login = self.login
        save_obj.port = self.port
        save_obj.servername = self.serverName
        save_obj.password = self.Password
        save_obj.tablename = self.tablename
        return save_obj