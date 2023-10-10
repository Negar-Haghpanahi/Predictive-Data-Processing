from inputclass import ReadRequest

class RequestBuilder_Read():

    def __init__(self):
        self.filepath =''
        self.readtype =''
        self.request =None
    
    def setfilepath(self, filepath):
        self.filepath=filepath
        return self

    def settype(self , type_):
        self.readtype =type_
        return self

    def create(self):
        self.request =ReadRequest()
        self.request.filepath=self.filepath
        self.request.read_type =self.readtype
        return self.request
        

        
        