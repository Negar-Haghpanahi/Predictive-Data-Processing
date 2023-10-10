from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from InputType.inputtype  import ModelPrediction
# from ModelPrediction.linearRegression import X
from inputclass import PridictModelRequest
from sklearn.metrics import mean_absolute_error
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import KFold 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class ModelContext():

    def __init__(self):
        pass
    # def executeModel(self,Model= ModelPrediction.decision_tree, df=None , target_col=None):
    def executeModel(self, classrequest:PridictModelRequest):
       
        if classrequest.df is not None and classrequest.pridictModel is not None: 
            if classrequest.pridictModel == ModelPrediction.decision_tree:
                ds_strategy=DS_Strategy(classrequest.df , classrequest.target_col , classrequest.splitdata_catidx)
                return ds_strategy.execute()
            elif classrequest.pridictModel == ModelPrediction.random_forest:
                rf_strategy=RF_Strategy(classrequest.df , classrequest.target_col , classrequest.splitdata_catidx)
                return rf_strategy.execute()



class ModelStrategy(ABC):

    def __init__(self ,dataframe , target , splitidx) -> None:
        self.df =dataframe
        self.target = target
        self.splitarray = splitidx
        self.X_train =None
        self.X_test  =None
        self.y_train =None
        self.y_test  =None
        self.TrinTestSplit()
    
    def TrinTestSplit(self):
        # X = self.df.iloc[:, 0:3].values
        X =self.df.iloc[:,self.splitarray]

        # y = self.df.iloc[:, 3].values
        y_idx = self.df.columns.get_loc(self.target) 
        y=self.df.iloc[:,y_idx]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        y=self.df[self.target]
        self.X_train=X_train
        self.X_test= X_test
        self.y_train = y_train
        self.y_test = y_test

    def execute(self):
        pass



#concrete stratigies
class DS_Strategy(ModelStrategy):
    
    def execute (self) :

        Model_tree= DecisionTreeRegressor(random_state=1)
        Model_tree.fit(self.X_train,self.y_train)
        Predictions=Model_tree.predict(self.X_test)
        print("predictions ")
        print(Predictions)
        print('----------')
        print( pd.DataFrame({'Real Values':self.y_test, 'Predicted Values':Predictions}))
        print('error is ')
        mean_error=mean_absolute_error(self.y_test,Predictions)
        print(mean_error) 
        return self.df
       

class RF_Strategy(ModelStrategy):

    def execute (self):
        sc = StandardScaler()
        print(self.df.dtypes)
        self.X_train = sc.fit_transform(self.X_train)
        self.X_test = sc.transform(self.X_test)
        regressor = RandomForestRegressor(n_estimators=20, random_state=0)
        regressor.fit(self.X_train, self.y_train)
        y_pred = regressor.predict(self.X_test)
        print("predictions ")
        print(y_pred)
        print('----------')
        print( pd.DataFrame({'Real Values':self.y_test, 'Predicted Values':y_pred}))
        print('error is ')
        mean_error=mean_absolute_error(self.y_test,y_pred)
        print(mean_error)
        return self.df


# if __name__ != "__main__":
#     data = pd.read_csv(r"C:\Users\asus\Desktop\New folder\dataset\src\datasetcsv\finalcsv.csv")
#     Context = context()
#     Context.executeModel(ModelPrediction.decision_tree,data , 'Rent')    
