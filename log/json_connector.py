import json
import mongoDB

class save_input():

    def __init__(self) -> None:
        self.input_req = None
        self.json_file = None
        self.remove_element = None

    def Prepare_json (self):
    
        self.remove_element =[input("Enter the featurse you want to drop to save into json format : \n")]

        # req = REQUEST_INPUT.remove_df (input_json,[remove_element])

    def remove_df(self , request ):          

        for key in self.remove_element:
            if key in request:
                del request[key]

        for value in request.values():
            if isinstance(value, dict):
                self.remove_df(value, self.remove_element)

        self.input_req = request
        
        return self.input_req

        # MND=mongoDB.MongoDB_saveto()
        # MND.save_to(this_dict)
        # return the id of 

    def Save_To_file(self):

        with open(r'C:\Users\asus\Desktop\work\dataset\src\SaveFile\test4.txt', 'w') as jsonfile:
            self.json_file =jsonfile 
            json.dump(self.input_req,jsonfile)    

    
# if __name__ == "__main__":

#     json_obj = json_()
#     x=input("tablename is\n")
#     json_obj.add_request(x)

#     type_idx =[int(x) for x in input().split()]
#     json_obj.add_request(type_idx)

#     json_obj.produce_file()



 # self.read_request =''
        # self.prepare_request =''
        # self.cluster_request =''
        # self.modelpridiction_request =''
        # self.relationalDB_request =''
        # self.prepareCheck_request =''
        # self.saverequest_request =''
