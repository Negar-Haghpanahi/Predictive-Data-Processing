from inputclass import InputClass_json

class Json_Builder():
    read_request =None
    prepare_request =None
    cluster_request =None
    modelpridiction_request =None
    relationalDB_request =None
    prepareCheck_request =None
    save_request =None
    NoneRelation_Mongo = None
    request =None

    def set_Read(self, read_req):
        
        self.read_request= read_req
        return self
    
    def set_Prepare(self, Prep_req):
        self.prepare_request = Prep_req
        return self

    def set_Cluster(self , cluster_req):
        self.cluster_request=cluster_req
        return self
    
    def set_Model(self , model_req):
        self.modelpridiction_request= model_req
        return self
    
    def set_RelationDB(self , RealDB_req):
        self.relationalDB_request=RealDB_req
        return self

    def set_Prep_Check(self , Prep_check_req):
        self.prepareCheck_request=Prep_check_req
        return self
    
    def set_Save(self , save_req):
        self.save_request=save_req
        return self
    
    def set_Mongo(self, Monog_req):
        self.NoneRelation_Mongo = Monog_req
        return self
    
    
    def create(self):
        request = InputClass_json()
        request.read_request = self.read_request
        request.prepare_request = self.prepare_request
        request.cluster_request = self.cluster_request
        request.modelpridiction_request = self.modelpridiction_request
        request.relationalDB_request = self.relationalDB_request
        request.prepareCheck_request = self.prepareCheck_request
        request.save_request= self.save_request
        request.NoneRelation_Mongo = self.NoneRelation_Mongo
        return request.__dict__


        






