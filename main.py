from cgitb import handler
import imp
from tkinter.messagebox import RETRY
from numpy import intp, true_divide
from pandas import DataFrame
from requests import request
from InputType.inputtype import context
from ChainPattern.chain1 import HandleContext
from ChainPattern.chain1 import ChainRequest
import inputclass
from InputType.inputtype import *
from Builder import DBbuilder
from Builder import Preparebuilder
from Builder import Pridictbuilder
from Builder import Clusterbuilder
from Builder import Readbuilder
from Builder import Savebuilder
from Builder import Jsonbuilder
from Builder import MongoDBbuilder
from Adapter import dict_Adapter
from log     import json_connector
from StrategyPattern.SaveStrategy import *
import json
#port = 3514 ipaddress='192.168.56.1'
#C:\Users\asus\Desktop\work\dataset\src\datasetcsv\housePrice.csv   
#C:\Users\asus\Desktop\work\dataset\src\datasetcsv\House_Rent_Dataset5.csv
#DESKTOP-F7TB0BK\MSSQLSERVER_13', 'sa', '****', "Sample"
#C:\Users\asus\Desktop\SMS\createfile\Final3.xlsx
#C:\Users\asus\Desktop\SMS\createfile\Final2.csv

def Show_cloumns(df : DataFrame):
    col_list =df.columns
    print("Here is the list of columns ")
    for i in range(0 , len(col_list)):
        print(i ,col_list[i])
    print(df.dtypes)


def Connect_database():
    servername ='DESKTOP-F7TB0BK\MSSQLSERVER_13' #input("servername is\n") 
    login ='sa'                                  #input("login is\n")
    password ='158619mn'                         #input("password is\n")
    dbname = 'SMS'                            #input("dbname is\n")
    tablename ='FINAL_TASK'                      #input("tablename is\n")
    request=DBbuilder.RequestBuilder_RelationDB().setServerName(servername).setLogin(login).setPassword(password).setDbname(dbname).setTablename(tablename).create()
    obj = dict_Adapter.DictConverter()
    obj.request_dict=request.__dict__        
    # json_obj.set_RelationDB(obj.__dict__)
    Create_Json(obj.__dict__)
    handel = HandleContext(context.connect , request)
    chain=ChainRequest(handel)
    return chain
   

def Read_File():
    filepath = input("Enter the file path ")
    readtype = int(input("Enter the file type\ncsv   1\nexcel 2\n"))
    request = Readbuilder.RequestBuilder_Read().setfilepath(filepath).settype(readtype).create()
    # json_obj.set_Read(createDict.Read_dict(request))                                   
    obj = dict_Adapter.DictConverter()
    obj.request_dict=request.__dict__
    # json_obj.set_Read(obj.__dict__)
    Create_Json(obj.__dict__)
    handel = HandleContext(context.read , request)
    chain=ChainRequest(handel)
    return chain


def Preparation(input_):
    if input_ ==prepare_.drop_column.value :
        col_name =input("Enter the column that you want to drop it \n")
        drop_request=Preparebuilder.Requestbuilder_Prepare().setdropcolumn(col_name).setmodel(prepare_.drop_column.name).create()                                   
        # json_obj.set_Prepare(createDict.Prepare_dict(drop_request))
        obj = dict_Adapter.DictConverter()
        obj.request_dict=drop_request.__dict__
        # json_obj.set_Prepare(obj.__dict__)
        Create_Json(obj.__dict__)
        handel = HandleContext(context.prepare , drop_request)  
        chain1=ChainRequest(handel)
        return chain1
    else:
        print("put in the indexes for type changing")
        type_idx =[int(x) for x in input().split()]
        type_request=Preparebuilder.Requestbuilder_Prepare().setlist(type_idx).setmodel(prepare_.change_type.name).create()
        # json_obj.set_Prepare(createDict.Prepare_dict(type_request))
        obj = dict_Adapter.DictConverter()
        obj.request_dict=type_request.__dict__
        # json_obj.set_Prepare(obj.__dict__)
        Create_Json(obj.__dict__)
        handel= HandleContext(context.prepare , type_request)  
        chain2=ChainRequest(handel)
        return chain2

def Clustering():
    target_col = input("enter the target column ")
    print("choose the clstering model\nk_means 1\nk_modes   2\nk_prototype    3")
    cluster_model = int(input("Enter the number of clustering model "))
    if cluster_model == clustering.k_prototype.value:
        print("Enter the categorical features indexs ")
        categorical_features_idx= [int(x) for x in input().split()]
        print("Enter the numerical index ")
        numerical_features_idx= [int(x) for x in input().split()]
        request=Clusterbuilder.Requestbuilder_Cluster().setModel(clustering.k_prototype.name).setTarget(target_col).setCategoricalidx(categorical_features_idx).setNumericidx(numerical_features_idx).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict=request.__dict__
        Create_Json(obj.__dict__)
        # json_obj.set_Cluster(obj.__dict__)
    elif cluster_model == clustering.k_means.value:      
        request=Clusterbuilder.Requestbuilder_Cluster().setModel(clustering.k_means.name).setTarget(target_col).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict=request.__dict__
        Create_Json(obj.__dict__)
        # json_obj.set_Cluster(obj.__dict__)
    else:
        print("Enter the categorical features indexs ")
        categorical_features_idx= [int(x) for x in input().split()]
        request=Clusterbuilder.Requestbuilder_Cluster().setModel(clustering.k_modes.name).setTarget(target_col).setCategoricalidx(categorical_features_idx).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict=request.__dict__
        Create_Json(obj.__dict__)
        # json_obj.set_Cluster(obj.__dict__)
    handel = HandleContext(context.cluster , request)
    chain2=ChainRequest(handel)
    return chain2
    

    ######### make the above !!!!!!!!!!!!!!!!!
def Model():    
    target_col = input("enter the target column ")
    print("enter the numerical indexes for spliting data ")
    categorical_split_idx= [int(x) for x in input().split()]
    pridict_model =int( input("choose the model of pridictions\nlinear_regression  1\ndecision_tree 2\nrandom_forest  3\n"))
    if pridict_model == ModelPrediction.linear_regression.value:
        request=Pridictbuilder.Requestbuilder_Pridict().setModel(ModelPrediction.linear_regression.name).setSplitidx(categorical_split_idx).setTarget(target_col).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict=request.__dict__
        Create_Json(obj.__dict__)
        # json_obj.set_Model(obj.__dict__)
    elif pridict_model ==ModelPrediction.decision_tree.value:
        request=Pridictbuilder.Requestbuilder_Pridict().setModel(ModelPrediction.decision_tree.name).setSplitidx(categorical_split_idx).setTarget(target_col).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict=request.__dict__
        Create_Json(obj.__dict__)
        # json_obj.set_Model(obj.__dict__)
    else:
        request=Pridictbuilder.Requestbuilder_Pridict().setModel(ModelPrediction.random_forest.name).setSplitidx(categorical_split_idx).setTarget(target_col).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict=request.__dict__
        Create_Json(obj.__dict__)
        # json_obj.set_Model(obj.__dict__)
    handel = HandleContext(context.model , request)
    chain3=ChainRequest(handel)
    return chain3


def Save():
    save_type = int(input("enter the type of file saving\nsave to csv 1\nsave to excel 2\nsave to db 3 \nSave to Mongodb 4\n"))
    if save_type==Save_file.save_to_csv.value:
        path =input("enter the file path ")
        request =Savebuilder.Save_Builder().set_path(path).set_type(Save_file.save_to_csv.name).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict=request.__dict__
        Create_Json(obj.__dict__)
        # json_obj.set_Save(obj.__dict__)
    elif save_type ==Save_file.save_to_excel.value:
        path =input("enter the file path ")
        request =Savebuilder.Save_Builder().set_path(path).set_type(Save_file.save_to_excel.name).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict=request.__dict__
        Create_Json(obj.__dict__)
        # json_obj.set_Save(obj.__dict__)
    elif save_type == Save_file.save_to_db.value:
        servername ='DESKTOP-F7TB0BK\MSSQLSERVER_13' #input("servername is\n") 
        login ='sa'                                  #input("login is\n")
        password ='158619mn'                         #input("password is\n")
        dbname = 'Sample'                            #input("dbname is\n")
        tablename ='housePrice'                      #input("tablename is\n")
        port ='3514'
        ipaddress ='192.168.56.1'
        request =Savebuilder.Save_Builder().setServerName(servername).setLogin(login).setPassword(password).setDbname(dbname).setTablename(tablename).setPort(port).setIPaddress(ipaddress).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict=request.__dict__
        json_dict=Create_Json(obj.__dict__)
        # json_obj.set_Save(obj.__dict__)
    else:                                                #save to mongodb
        client_name  ='localhost'             #input("The client name is?\n")
        URI_num = '27107'                     #input("The URI IS ?\n")
        Mongo_dbname = 'ML_DB'                #input("THE db name is ?\n")
        collection_name = 'INPUT_DATA'        #input("Collection name is ?\n")
        request = MongoDBbuilder.Mongo_builder().set_client(client_name).set_URI(URI_num).set_dbname(Mongo_dbname).set_collection(collection_name).set_inputjson(json_dict).create()
        obj = dict_Adapter.DictConverter()
        obj.request_dict = request.__dict__
        json_dict = Create_Json(obj.__dict__)
        
        # json_obj.NoneRelation_Mongo (json_obj.create())                
        mongo_save = Save_To_Mongo(request)
    handel = HandleContext(context.save_file , request)        
    chain3=ChainRequest(handel) 
    return chain3


if __name__ == "__main__":

    # json_obj =Jsonbuilder.Json_Builder()
    lst=[]
    flag = input("HELLO if you want to start the program , enter 1 \nelse , for leaving enter 0--> \n")
    
    option = int(input("put in the number\n1 read the file\n2 connect to database\n"))
    if option ==Readtype.Read_database.value :
        chain=Connect_database()
        lst.append(chain)
        chain.handle(None)
        df=chain._context.request.df
        Show_cloumns(df)                                   
        Readrequest = chain._context.request
    else:
        chain =Read_File()
        lst.append(chain)
        chain.handle(None)
        df=chain._context.request.df
        Show_cloumns(df)                                         
        Readrequest = chain._context.request

    while flag:
        
        request_num = int(input("Please choose your request from the list above (enter only the number)\npreper the file  2\ncluster the file 3\npridict model    4\nsave file 5\n"))
        if  request_num == context.prepare.value :
            val =1
            while val:
                input_ =int(input("drop columns --> 1\nchange the type of column --> 2\n"))
                chain=Preparation(input_)
                lst.append(chain)
                val =int(input("set the value do it again 1 else 0\n"))
    
        elif request_num == context.cluster.value :
            Show_cloumns(df)
            chain =Clustering()
            lst.append(chain)
        elif request_num == context.model.value :
            Show_cloumns(df)
            chain =Model()
            lst.append(chain)
        else :
            chain = Save() 
            lst.append(chain)      

        flag = int(input("set the flag "))


    for i in range(0,len(lst)-1):
        chain=lst[i]
        next_chain=lst[i+1]
        chain.set_next(next_chain)
    chain=lst[0]
    chain.handle()
    


    


#C:\Users\asus\Desktop\New folder\df_saveto\houseprice_save.csv




















    

