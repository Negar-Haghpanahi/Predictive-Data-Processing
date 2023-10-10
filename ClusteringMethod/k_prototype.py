from statistics import mode
import pandas
import inputtype 
import ReadingFile
from kmodes.kprototypes import KPrototypes
from kmodes.kprototypes import kmodes
# from kmodes.kprototypes import Kmeans



class Clustering():
    def __init__(self , dataframe , categorical_list_idx ,target , model=inputtype.clustering.k_prototype ):
        self.df = dataframe
        self.X= target
        self.clustering = model
        self.df=self.calculate(model , categorical_list_idx , self.X)
    
    def calculate(self , model , list , target):

        if model == inputtype.clustering.k_prototype:
            object_prep=ReadingFile.Preparation(self.df)
            df = ReadingFile.Preparation(self.df).dropColumns(self.df ,self.X)
            mark_array = self.df.values
            count= len(list)
            for i in range (0 , count):
                mark_array[:, list[i]] = mark_array[: , 1].astype(float)
            kproto = KPrototypes(n_clusters=3 , verbose=2, max_iter=20)
            cluster =kproto.fit(mark_array, categorical=list)
            cluster_dict =[]
            for  i in cluster.labels_:
                cluster_dict.append(i)

            self.df=ReadingFile.Preparation(self.df).addColumn(self.df , target , self.X.value)
            self.df=ReadingFile.Preparation.addColumn(self.df ,'cluster' , cluster_dict)

            if self.df['cluster']==0:
                self.df=ReadingFile.Preparation.addColumn(self.df ,'cluster_0' , 0 )
            elif self.df['cluster']==1:
                self.df=ReadingFile.Preparation.addColumn(self.df ,'cluster_1' , 1 )
            else:
                self.df=ReadingFile.Preparation.addColumn(self.df ,'cluster_2' , 2 )
            
            self.df["cluster_0"] = self.df["cluster_0"].astype(int)
            self.df["cluster_1"] = self.df["cluster_1"].astype(int)
            self.df["cluster_2"] = self.df["cluster_2"].astype(int)

        return self.df

