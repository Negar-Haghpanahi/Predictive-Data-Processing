from cgi import print_form
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

df=pd.read_csv(r'C:\Users\asus\Desktop\New folder\dataset\House_Rent_Dataset5.csv')
# print(df.info())
df = df.dropna(axis=0)
df=df.drop('Posted On' , axis=1)
# counting distinct values for categorical columns
# print(len (df['Floor'].unique()))  # 480
# print(len (df['Area Locality'].unique())) #2233
# print(len (df['City'].unique())) #6
# print(len (df['Furnishing Status'].unique())) #3
# print(len (df['Tenant Preferred'].unique())) #3
# print(len (df['Point of Contact'].unique())) #3
 
# now drop the columns which involve high variety
df = df.drop('Area Locality' , axis=1)

X = df
y = df['Floor']

#converting categorical columns into integers
le = LabelEncoder()

X['Floor'] = le.fit_transform(X['Floor'])

y = le.transform(y)

print(X.info())
columns=X.columns
print(X.head())

ms = MinMaxScaler()
X = ms.fit_transform(X)
X = pd.DataFrame(X, columns=[columns])
print(X.haed())
kmeans = KMeans(n_clusters=3, random_state=0) 

# kmeans.fit(X)

# print(kmeans.cluster_centers_)





