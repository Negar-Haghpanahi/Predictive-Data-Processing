from inputclass import MongoDBRequest

class Mongo_builder():
    
    connect_type = None
    URI = None
    client = None
    mongodb_name = None
    collection_name = None
    input_json = None

    def set_type(self, type_name):
        self.connect_type = type_name
        return self

    def set_URI(self, uri):
        self.URI = uri
        return self
    
    def set_client(self , client_name):
        self.client = client_name
        return self

    def set_dbname(self , dbname):
        self.mongodb_name = dbname
        return self
    def set_collection(self , collection):
        self.collection_name = collection
        return self

    def set_inputjson(self, json_input):
        self.input_json = json_input
        return self



    def create(self):
        request = MongoDBRequest()
        request.connect_type = self.connect_type
        request.client = self.client
        request.collection_name = self.collection_name
        request.URI = self.URI
        request.mongodb_name = self.mongodb_name
        request.input_json = self.input_json
        return request.__dict__