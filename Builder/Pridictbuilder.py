from statistics import mode
from inputclass import PridictModelRequest

class Requestbuilder_Pridict():

    def __init__(self) -> None:
        self.model =''
        self.target=''
        self.split_idx=''
        self.request=None

    def setModel(self , model):
        self.model=model
        return self

    def setTarget(self, target):
        self.target=target
        return self

    def setSplitidx(self , splitidx):
        self.split_idx =splitidx
        return self

    def create(self):
        self.request =PridictModelRequest()
        self.request.target_col =self.target
        self.request.pridictModel=self.model
        self.request.splitdata_catidx =self.split_idx
        return self.request
