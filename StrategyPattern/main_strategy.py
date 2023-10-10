import pandas as pd
import Strategy1
import inputtype


data = pd.read_csv(r"C:\Users\asus\Desktop\New folder\dataset\finalcsv.csv")
print(data.columns)
target_column=input ("Here is the column list of data frame , enter the target column name ! ")
print("choose the model  validation : ")
model_num=input(" linear_regression = 1  decision_tree = 2 random_forest = 3    --> ")

if model_num == 1:
    model_val= inputtype.ModelPrediction.linear_regression
elif model_num ==2:
    model_val=inputtype.ModelPrediction.decision_tree
else:
    model_val =inputtype.ModelPrediction.random_forest

strategy_obj = Strategy1.context()
strategy_obj.executeModel(model_val ,data , target_column)    



