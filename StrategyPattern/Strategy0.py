from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import inputtype

data = pd.read_csv(r"C:\Users\asus\Desktop\New folder\dataset\finalcsv.csv")

class context():
    strategy: ModelStrategy

    def setStrategy (self,Model, strategy: ModelStrategy = None) -> None:
        if strategy is not None:
            self.strategy=strategy
            if Model == inputtype.ModelPrediction.decision_tree:
                DS_Strategy.execute (ModelStrategy)
            elif Model == inputtype.ModelPrediction.random_forest:
                RF_Strategy.exeute(ModelStrategy)
                 
        
class ModelStrategy(ABC):
    @abstractmethod
    def __init__(self ,dataframe , modelname ) -> None:
        self.model=modelname
        self.df =dataframe
        self.X_train = self.df.Rent
        self.X_test  =self.df.Rent
        self.y_train =self.df.Rent
        self.y_test  =self.df.Rent

    def TrinTestSplit(self):

        X = self.df.iloc[:, 0:4].values
        y = self.df.iloc[:, 4].values 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        y=self.df.Rent
        self.X_train=X_train
        self.X_test= X_test
        self.y_train = y_train
        self.y_test = y_test

    def exeute (df):   #add class
        pass

#concrete stratigies
class DS_Strategy(ModelStrategy):
    
    def execute (self , dataframe) :
        self.df=dataframe
        Model_tree= DecisionTreeRegressor(random_state=1)
        Model_tree.fit(self.X_train,self.y_train)
        Predictions=Model_tree.predict(self.X_test)
        print("predictions ")
        print(Predictions)

class RF_Strategy(ModelStrategy):

    def execute (self , dataframe):
        
        sc = StandardScaler()
        self.X_train = sc.fit_transform(self.X_train)
        self.X_test = sc.transform(self.X_test)
        regressor = RandomForestRegressor(n_estimators=20, random_state=0)
        regressor.fit(self.X_train, self.y_train)
        y_pred = regressor.predict(self.X_test)
        print("predictions ")
        print(y_pred)

 

if __name__ == "__main__":

    context = context(DS_Strategy().execute(data))
    context.setStrategy('decision_tree' )


    



# object_con=context.setStrategy('decision_tree' )

# context(DS_Strategy(data ,'decision_tree' ))

