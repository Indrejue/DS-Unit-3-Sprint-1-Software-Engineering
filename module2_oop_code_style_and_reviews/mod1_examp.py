""" helper function for Data science """

#importing libraries for function into the package
import pandas as pd
import numpy as np 

class MyDataFrame(pd.DataFrame):
    
    # define a null count function
    def nulls(self):
        count = self.isnull().sum()
        return count

    #create a date split function.
    def date_split(self):
        self['col'] = self.select_dtypes('datetime')
        self['year'] = self['col'].dt.year
        self['month'] = self['col'].dt.month
        self['day'] = self['col'].dt.day
        self = self.drop(columns='col')
        return self