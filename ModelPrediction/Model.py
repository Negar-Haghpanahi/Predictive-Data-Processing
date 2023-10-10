import inputtype
import clustering
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


class Models():


    def __init__(self ,dataframe , Feature_Names , model = inputtype.ModelPrediction.decision_tree):
        self.model = model
        self.df = dataframe
        self.Feature_Names=Feature_Names
        if self.model == inputtype.ModelPrediction.random_forest:
            self.random_forest()
        elif self.model == inputtype.ModelPrediction.decision_tree:
            self.decision_tree()
        
    def random_forest(self):
        print('random_forest')

    def decision_tree(self):
        y=self.df.Rent
        X=self.df[ self.Feature_Names]
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        Model_tree= DecisionTreeRegressor(random_state=1)
        Model_tree.fit(X_train,y_train)
        Predictions=Model_tree.predict(X_test)
        print("predictions ")
        print(Predictions)
