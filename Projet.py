import logging
logging.basicConfig(filename='test_log.log',level=logging.INFO,format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import math
import numpy as np
from py2neo import Graph, Relationship, Node
#pd.set_option('display.max_rows', None)
#from sklearn.preprocessing import LabelEncoder

from PyCharm.fonction import fctdf
pd.set_option('display.max_rows', 1000)

data="C:/Users/A.NGUYENCAO/Documents/Repo_G2_Dataset_9_cost/Dataset_9_cost.csv"
df=pd.read_csv(data, sep="|")

listecoldrop=["Unnamed: 0","Unnamed: 0.1","Unnamed: 0.1.1","Unnamed: 0.1.1.1","Unnamed: 0.1.1.1.1","Unnamed: 0.1.1.1.1.1","Unnamed: 0.1.1.1.1.1.1","Unnamed: 0.1.1.1.1.1.1.1","Unnamed: 0.1.1.1.1.1.1.1.1"]
listecolchain=["Allez au boulot ! :)","55555555555","courage!!!","ù*ùfsfsf///","0","None"]

df = fctdf.dropcol(df,listecoldrop)

df = fctdf.traitcolflo(df,"age")
df = fctdf.traitcolflo(df,"bmi")
df = fctdf.traitcolflo(df,"children")
df = fctdf.traitcolflo(df,"charges")

df = fctdf.traitcolstr(df,"sex")
df = fctdf.traitcolstr(df,"smoker")
df = fctdf.traitcolstr(df,"region")

df = fctdf.traitcolsmok(df,"sex")
df = fctdf.traitcolsmok(df,"smoker")
df = fctdf.traitcolsmok(df,"region")

print(df)

fctdf.predrf(df,10)




df.drop(df.columns[[0, 1, 24, 25, 26, 27, 28, 29, 30]], axis=1, inplace=True)

graph = Graph("http://localhost:7474/")

g = graph()
g.delete_all()

for c in df["charges"]:
   charges = Node("charges", name=c)
   graph.create(charges)
   for a in df["age"]:
    age = Node("age", name=a)
    graph.create(age)
    for s in df["sex"]:
     sex = Node("sex", name=s)
     graph.create(sex)


r1 = Relationship(charges, "Relations", age)
graph.create(r1)
r2 = Relationship(age, "Relations", sex)
graph.create(r2)

