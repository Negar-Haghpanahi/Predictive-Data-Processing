# # # import json
# # from Adapter import dict_Adapter

# # class input_json():
    
# #     def __init__ (self):
# #         self.target = 'Rent'
# #         self.type_add = 'csv'
# #         self.num_idx = [1 , 2 , 3]

# #     # def __iter__(self):
# #     #     for key in self.__dict__: #self.type_add:
# #     #         yield (key ,'value {}'.format(key))


# # input_obj = input_json()
# # obj = dict_Adapter.convert_to_dict()
# # obj.request_dict=input_obj.__dict__
# # print(obj.__dict__)
# # # print(input_obj.__dict__)
# # print(dict(obj))
    

# # if __name__ == "__main__":

# #     obj = input_json()
# #     # obj.get_input()
# #     this_dict = obj.__dict__
# #     print(this_dict)


# #     # with open(r'C:\Users\asus\Desktop\New folder\dataset\src\SaveFile\text2.txt', 'w') as json_file:
# #     #     json.dump(this_dict,json_file)
# #     # y = json.dumps(this_dict)
# #     # print(y)



# # my_dic = {'request_dict': {'df':5466 , 'target_col': None, 'filepath': 'C:\\Users\\asus\\Deskto...ePrice.csv', 'read_type': 1}}

# # my_dic ={'df': None, 'target_col': None, 'read_request': {'request_dict':{'df':5466 , 'target_col': None, 'filepath': 'C:\\Users\\asus\\Deskto...ePrice.csv', 'read_type': 1}}
# #                 , 'prepare_request': {'request_dict': 76 }, 'cluster_request': None, 'modelpridiction_request': None, 'relationalDB_request': None, 'prepareCheck_request': None, 'save_request': None }





# def remove_nested_keys(dictionary, keys_to_remove):
#     for key in keys_to_remove:
#         if key in dictionary:
#             del dictionary[key]

#     for value in dictionary.values():
#         if isinstance(value, dict):
#             remove_nested_keys(value, keys_to_remove)

#     return dictionary

# my_dic ={'df': None, 'target_col': None, 'read_request': {'request_dict':{'df':5466 , 'target_col': None, 'filepath': 'C:\\Users\\asus\\Deskto...ePrice.csv', 'read_type': 1}}
#                 , 'prepare_request': {'request_dict': 76 }, 'cluster_request': None, 'modelpridiction_request': None, 'relationalDB_request': None, 'prepareCheck_request': None, 'save_request': None }

# # 👇️ {'address': {'country': 'Finland'}, 'name': 'Frank'}
# x = input("name of element : ")
# print(remove_nested_keys(my_dic, [x]))


import pymongo
import pandas as pd
from pymongo import MongoClient

client = MongoClient()

#point the client at mongo URI
client = MongoClient('localhost', 27017)
#select database
db = client['ML_DB']
collection = db['INPUT_DATA']
#select the collection within the database
# test = db.ML_DB.INPUT_DATA
#convert entire collection to Pandas dataframe
test = pd.DataFrame(list(collection.find()))
print(test)