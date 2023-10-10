from enum import Enum

from numpy import DataSource


#from statistics import linear_regression

class context(Enum):
    
    connect = 0
    read    = 1
    prepare = 2
    cluster = 3
    model   = 4
    save_file = 5
    convert_to_json = 6

class type_(Enum):

    csv   = 1
    excel = 2
    

class Readtype(Enum):
    Read_file = 1
    Read_database = 2


class clustering(Enum):
    k_means = 1
    k_modes = 2
    k_prototype =3

class prepare_(Enum):
    drop_column = 1
    change_type = 2

class ModelPrediction (Enum):
    linear_regression = 1
    decision_tree = 2
    random_forest = 3


class Save_file(Enum):
    save_to_csv = 1
    save_to_excel = 2
    save_to_db = 3
    save_to_mongoDB = 4

