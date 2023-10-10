import csv
from mimetypes import init
from typing import Type
import numpy as np
import pandas as pd
import os
import InputType.inputtype 


class READ_FILE():

    def __init__(self, FilePath, type=inputtype.type_.csv):
        self.FilePath=FilePath
        self.df=self.CheckType(type)
        
    def CheckType(self,_type):
        if _type ==inputtype.type_.csv:
            df=pd.read_csv(self.FilePath)

        elif _type == inputtype.type_.excel:             
            df=pd.read_excel(self.FilePath)
            
        return df

    def getDataframe(self):
        return self.df

class Preparation():
    def __init__(self  , df):
        self.dataframe=df
        #  self.dataframe=
        self.dropRows(self.dataframe)

    def dropRows(self , dataframe) :
        self.dataframe=dataframe.dropna(axis=0)
        # return self.dataframe

    def dropColumns(self, df, colname):
        self.dataframe=df
        self.dataframe=df.drop(colname , axis=1)
        # return self.df

    def addColumn(self , df , colname , value):
        self.dataframe=df
        self.dataframe[colname]=value
        # return self.df




        
    
        
    

    


    
