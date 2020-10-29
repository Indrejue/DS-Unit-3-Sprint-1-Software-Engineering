""" helper function for Data science """

#importing libraries for function into the package
import pandas as pd
import numpy as np 

class MyDataFrame(pd.DataFrame):
      
    # define a null count function
    def nulls(self):
        count = self.isnull().sum().sum()
        return count

    #create a date split function.
    def date_split(self):
        self['col'] = self.select_dtypes('datetime')
        self['year'] = self['col'].dt.year
        self['month'] = self['col'].dt.month
        self['day'] = self['col'].dt.day
        self = self.drop(columns='col')
        return self

# df1 = pd.read_csv('https://raw.githubusercontent.com/Indrejue/DS-Unit-2-Applied-Modeling/master/data/burritos/burritos.csv', parse_dates=['Date'])

# cols = df1.columns
# values = df1.values

# testdf = MyDataFrame(columns=cols,data=values)

# print(testdf.head())
# print(df1.isnull().sum().sum())

# print(testdf.nulls())