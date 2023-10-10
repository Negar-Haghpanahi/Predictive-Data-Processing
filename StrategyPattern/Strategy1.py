from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import InputType.inputtype  import ModelPrediction


class context():

    def __init__(self):
        pass
    def executeModel(self,Model= ModelPrediction.decision_tree, df=None , target_col=None):
        if df is not None and Model is not None: 
            if Model == ModelPrediction.decision_tree:
                ds_strategy=DS_Strategy(df , target_col)
                ds_strategy.execute()
            elif Model == ModelPrediction.random_forest:
                rf_strategy=RF_Strategy(df , target_col)
                rf_strategy.execute()



class ModelStrategy(ABC):

    def __init__(self ,dataframe , target) -> None:
        self.df =dataframe
        self.target = target
        self.X_train = self.df[target]
        self.X_test  =self.df[target]
        self.y_train =self.df[target]
        self.y_test  =self.df[target]
        self.TrinTestSplit()
    
    def TrinTestSplit(self):

        X = self.df.iloc[:, 0:4].values
        y = self.df.iloc[:, 4].values 
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

class RF_Strategy(ModelStrategy):

    def execute (self):
        sc = StandardScaler()
        self.X_train = sc.fit_transform(self.X_train)
        self.X_test = sc.transform(self.X_test)
        regressor = RandomForestRegressor(n_estimators=20, random_state=0)
        regressor.fit(self.X_train, self.y_train)
        y_pred = regressor.predict(self.X_test)
        print("predictions ")
        print(y_pred)


if __name__ == "__main__":
    data = pd.read_csv(r"C:\Users\asus\Desktop\New folder\dataset\finalcsv.csv")
    Context = context()
    Context.executeModel(ModelPrediction.decision_tree,data , 'Rent')    
