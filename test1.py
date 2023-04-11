import pandas as pd 
import numpy as np
import os

currentpath = os.getcwd()
A = pd.read_csv("abc12.csv")
#A = pd.read_csv("test11.csv")
#data = pd.read_csv("test11.csv")

#print(A)

data=pd.merge(A, on="user")
column=['user', 'movieA', 'movieB', 'movieC', 'movieD', 'movieE']
data=data[column]
data


추가용