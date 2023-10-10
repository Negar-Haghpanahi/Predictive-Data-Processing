from statistics import mode
from turtle import pensize
import pandas
import inputtype 
import ReadingFile
from kmodes.kprototypes import KPrototypes
from kmodes.kprototypes import kmodes
# from kmodes.kprototypes import Kmeans



class Cluster():
    def __init__(self , dataframe , categorical_list_idx ,target ,value ,model=inputtype.clustering.k_prototype ):
        self.df = dataframe
        self.X= target
        self.y=value
        self.clustering = model
        self.df=self.calculate(model , categorical_list_idx , self.X)
    
    def calculate(self , model , list , target):

        if model == inputtype.clustering.k_prototype:
            object_prep =ReadingFile.Preparation(self.df)
            object_prep.dropColumns(self.df ,self.X)
            mark_array = object_prep.dataframe.values
            # count= len(list)
            # for i in range (0 , count):
            #     mark_array[:, list[i]] = mark_array[: , 1].astype(float)
            mark_array[:, 0] = mark_array[: , 1].astype(float)
            mark_array[:, 1] = mark_array[: , 1].astype(float)
            mark_array[:, 8] = mark_array[: , 1].astype(float)
            mark_array[:, 10] = mark_array[: , 1].astype(float)
            mark_array[:, 13] = mark_array[: , 1].astype(float)
            mark_array[:, 14] = mark_array[: , 1].astype(float)
            mark_array[:, 15] = mark_array[: , 1].astype(float)
            kproto = KPrototypes(n_clusters=3 , verbose=2, max_iter=20)
            cluster =kproto.fit(mark_array, categorical=list)
            cluster_dict =[]
            for  i in cluster.labels_:
                cluster_dict.append(i)

            object_prep.addColumn(object_prep.dataframe , target , self.y)
            object_prep.addColumn(object_prep.dataframe ,'cluster' , cluster_dict)
            object_prep.addColumn(object_prep.dataframe ,'cluster_0' , 5) 
            object_prep.addColumn(object_prep.dataframe ,'cluster_1' , 6)
            object_prep.addColumn(object_prep.dataframe,'cluster_2' , 7)
            print("cluster")
            print(object_prep.dataframe)
            self.df = object_prep.dataframe

            self.df['cluster_0'] =self.df['cluster']==0
            self.df['cluster_1'] =self.df['cluster']==1
            self.df['cluster_2'] =self.df['cluster']==2

            #     self.df=ReadingFile.Preparation(self.df).addColumn(self.df ,'cluster_0' , 0 )
            # elif self.df['cluster']==1:
            #     self.df=ReadingFile.Preparation(self.df).addColumn(self.df ,'cluster_1' , 1 )
            # else:
            #     self.df=ReadingFile.Preparation(self.df).addColumn(self.df ,'cluster_2' , 2 )
            # print(self.df)

            self.df["cluster_0"] = self.df["cluster_0"].astype(int)
            self.df["cluster_1"] = self.df["cluster_1"].astype(int)
            self.df["cluster_2"] = self.df["cluster_2"].astype(int)
        print("--------")
        print(self.df)
        return self.df

