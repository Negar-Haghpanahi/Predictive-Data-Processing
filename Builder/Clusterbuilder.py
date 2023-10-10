from inputclass import ClusterRequest

class Requestbuilder_Cluster():

    def __init__(self) -> None:
        self.model=''
        self.target=''
        self.categorical_idx =''
        self.numeric_idx=''
        self.request =None

    def setModel(self, model):
        self.model =model
        return self
    
    def setTarget(self, target):
        self.target=target
        return self

    def setCategoricalidx(self , catidx):
        self.categorical_idx=catidx
        return self
    
    def setNumericidx(self , numidx):
        self.numeric_idx=numidx
        return self
    
    def create(self):
        self.request = ClusterRequest()
        self.request.categorical_features_idx=self.categorical_idx
        self.request.clusterModel=self.model
        self.request.numerical_idx=self.numeric_idx
        self.request.target_col=self.target
        return self.request





