from statistics import mode
from turtle import pensize
from unicodedata import numeric
from InputType.inputtype import clustering
from InputType.inputtype import ModelPrediction
from kmodes.kprototypes import KPrototypes
from kmodes.kprototypes import kmodes
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score
from abc import ABC, abstractmethod
from inputclass import ClusterRequest
from sklearn.feature_selection import chi2
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



class Clustercontext():

    def __init__(self):
        pass

    # def executeCluster(self, df=None ,  target_col=None , Model = clustering.k_prototype):  #inputtttt
    def executeCluster(self , classrequest:ClusterRequest):
        
        
        if classrequest.df is not None and classrequest.clusterModel is not None: 
            if classrequest.clusterModel == clustering.k_prototype:

                kpro_strategy=kprototype_Strategy(classrequest)  
                return kpro_strategy.execute()

            elif classrequest.clusterModel == clustering.k_modes:
                kmeans_strategy=kmodes_Strategy(classrequest)
                return kmeans_strategy.execute()

            else :
                kmeans_strategy=kmeans_Strategy(classrequest)
                return kmeans_strategy.execute()



class ClusterStrategy(ABC):

    def __init__(self ,classrequest:ClusterRequest ) -> None:
        self.request = classrequest
        
    def execute(self):
        pass

#concrete stratigies
class kprototype_Strategy(ClusterStrategy):
    
    def execute (self) :
            categorical_features_idx =self.request.categorical_features_idx
            num_idx = self.request.numerical_idx
            self.y= self.request.df[self.request.target_col]
            self.df = self.request.df.drop(self.request.target_col , axis = 1)
            lst = self.request.df.columns
            mark_array = self.request.df.values
            for i in range (0 , len(num_idx)):
                x = num_idx[i]
                mark_array[:, x] = mark_array[: , x].astype(float)    
        
            kproto = KPrototypes(n_clusters=3 , verbose=2, max_iter=20)
            cluster =kproto.fit(mark_array, categorical= categorical_features_idx)
            cluster_dict =[]
            for  i in cluster.labels_:
                cluster_dict.append(i)

            self.df[self.request.target_col] =self.y
            self.df['cluster'] =cluster_dict
            self.df['cluster_0'] =5
            self.df['cluster_1'] = 6
            self.df['cluster_2'] = 7

            print("cluster")
            print(self.df)

            self.df['cluster_0'] =self.df['cluster']==0
            self.df['cluster_1'] =self.df['cluster']==1
            self.df['cluster_2'] =self.df['cluster']==2

            self.df["cluster_0"] = self.df["cluster_0"].astype(int)
            self.df["cluster_1"] = self.df["cluster_1"].astype(int)
            self.df["cluster_2"] = self.df["cluster_2"].astype(int)
            print("--------")
            print(self.df.dtypes)
            print(self.df)
            return self.df     

class kmodes_Strategy(ClusterStrategy):

    def execute(self):
        return super().execute()



class kmeans_Strategy(ClusterStrategy):
    def execute(self):
        self.y= self.request.df[self.request.target_col]
        self.df = self.request.df.drop(self.request.target_col , axis =1)
        scaled_df = StandardScaler().fit_transform(self.df)
        kmeans_kwargs = { "init": "random","n_init": 10,"random_state": 1, }
        sse = []
        for k in range(1, 11):
            kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
            kmeans.fit(scaled_df)
            sse.append(kmeans.inertia_)
        kmeans = KMeans(init="random", n_clusters=3, n_init=10, random_state=1)
        kmeans.fit(scaled_df)
        kmeans.labels_
        self.df[self.request.target_col] =self.y
        self.df[self.request.target_col]=self.df[self.request.target_col].astype(int)  #??????????
        self.df['cluster'] = kmeans.labels_
        print("K_Means clustering")
        print(self.df)
        return self.df





# if __name__ != "__main__":
#     data = pd.read_csv(r"C:\Users\asus\Desktop\New folder\dataset\datasetcsv\finalcsv.csv")
#     Context = context()
#     Context.executeCluster(ModelPrediction.decision_tree,data , 'Rent')    
