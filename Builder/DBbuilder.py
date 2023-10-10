from inputclass import RelationalDBRequest

class RequestBuilder_RelationDB():
    def __init__(self):
        self.serverName=''
        self.dbname=''
        self.login=''
        self.Password=''
        self.tablename=''
        self.request=None

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
        
    def create(self):
        self.request=RelationalDBRequest()
        self.request.servername=self.serverName
        self.request.dbname=self.dbname
        self.request.login=self.login
        self.request.password=self.Password
        self.request.tablename=self.tablename

        return self.request

# if __name__=='__main__':
#     servername = "DESKTOP-F7TB0BK\MSSQLSERVER_13"   #input("servername is\n") 
#     login = "sa"                                   # input("login is\n")
#     password ="158619mn"                        #   input("password is\n")
#     dbname =  "Sample"                                 #input("dbname is\n")
#     tablename = "housePrice"    
    # request=RequestBuilder().setDB('').setServerName('test').create()
