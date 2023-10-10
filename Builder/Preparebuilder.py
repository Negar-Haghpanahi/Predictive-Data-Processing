import re
from symbol import return_stmt
from matplotlib.pyplot import cla
from pyparsing import col
from requests import request
from inputclass import PrepRequest
from inputclass import PrepareCheck
from InputType.inputtype import prepare_

class Requestbuilder_Prepare():
    def __init__(self) :
        self.column =''
        self.index_list=''
        self.type_ =''
        self.request =None
    
    def setmodel(self, model):
        self.type_ = model
        return self

    def setdropcolumn(self, columnname):
        self.column =columnname
        return self
        
    def setlist(self , idxlist):
        self.index_list = idxlist
        return self
    
    
    def create(self):
        self.request = PrepareCheck()
        self.request.dropcolumn= self.column
        self.request.list =self.index_list
        self.request.model =self.type_
        return self.request