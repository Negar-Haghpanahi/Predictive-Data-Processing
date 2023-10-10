

class Create_Dict():


    def Read_dict(self , request:inputclass.ReadRequest):

        result={}
        result['filepath']=request.filepath
        return  result   
  
    def Prepare_dict(self ,request:inputclass.PrepareCheck):  #checkkkkkkkkkkkkkkkkkkkk
    
        result={}
        result['column_name']  =request.dropcolumn
        result['list_of_idx']  =request.list      
        # result['type_of_prep'] =request
        return   result       

    def Cluster_dict(self , request:inputclass.ClusterRequest):

        result={}
        result['cluster_model']            =request.clusterModel
        result['target_col']               =request.target_col
        result['categorical_features_idx'] =request.categorical_features_idx
        result['numerical_idx']            =request.numerical_idx
        return  result 

    def Pridict_dict(self , request :inputclass.PridictModelRequest):
        result={}
        result['pridict_Model']   = request.pridictModel
        result['target_col']      = request.target_col
        result['splitdata_catidx']= request.splitdata_catidx
        return result

    def DBrequest_dict(self , request : inputclass.RelationalDBRequest):
        result={}
        result['server_name'] =request.servername
        result['login']       =request.login
        result['password']    =request.password
        result['DB_name']     =request.dbname
        result['table_name']  =request.tablename
        return result

    def Prepcheck_dict(self , request : inputclass.PrepareCheck):

        result={}
        result['dropcolumn'] =request.dropcolumn
        result['model']      =request.model
        result['list']       =request.list
        return result

    def Save_dict(self , request :inputclass.SaveRequest):
        
        result={}
        result['save_model'] =request.savemodel
        result['file_path']  =request.filepath
        result['serve_name'] =request.servername
        result['DB_name']    =request.dbname
        result['login']      =request.login
        result['password']   =request.password
        result['table_name'] =request.tablename
        result['ip_address'] =request.ipaddress
        result['port']       =request.port
        return result

    # def json_dict(self):

    #     result={}
    #     result['read_request']           =self.Read_dict()
    #     result['prepare_request']        =self.Prepare_dict()
    #     result['cluster_request']        =self.Cluster_dict()
    #     result['modelpridiction_request']=self.Pridict_dict()
    #     result['relationalDB_request']   =self.DBrequest_dict()
    #     result['prepareCheck_request']   =self.Prepcheck_dict()
    #     result['saverequest_request']    =self.Save_dict()
    #     return result

