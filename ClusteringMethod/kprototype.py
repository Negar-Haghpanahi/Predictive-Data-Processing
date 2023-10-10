import numpy as np
import pandas as pd
from kmodes.kprototypes import KPrototypes
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score

df = pd.read_csv(r'C:\Users\asus\Desktop\New folder\dataset\House_Rent_Dataset5.csv')
df=df.drop('Posted On' , axis=1)
df=df.drop('Rent' , axis=1)
df = df.dropna(axis = 0)
print(df.shape)
print(df.head())
#[4 , 5 , 6 , 7 , 8 , 9 , 11]

categorical_features_idx = [2, 3 , 4 , 5 , 6 , 7  , 9 ]
mark_array = df.values
print(df.values)
mark_array[:, 0] = mark_array[: , 1].astype(float)
mark_array[:, 1] = mark_array[: , 1].astype(float)
mark_array[:, 8] = mark_array[: , 1].astype(float)
mark_array[:, 10] = mark_array[: , 1].astype(float)
mark_array[:, 13] = mark_array[: , 1].astype(float)
mark_array[:, 14] = mark_array[: , 1].astype(float)
mark_array[:, 15] = mark_array[: , 1].astype(float)
#mark_array[:, 16] = mark_array[: , 1].astype(float)

kproto = KPrototypes(n_clusters=3 , verbose=2, max_iter=20)
cluster =kproto.fit(mark_array, categorical=categorical_features_idx)
print('-------------')
print(kproto.cluster_centroids_)
print('-------------')
cluster_dict =[]
for  i in cluster.labels_:
    cluster_dict.append(i)

df['cluster']=cluster_dict

#add clusters into new columns

df['cluster_0'] =df['cluster']==0
df['cluster_1'] =df['cluster']==1
df['cluster_2'] =df['cluster']==2

