#import json
#import pandas as pd

#with open("C:/Users/Antoine/Documents/Repo_NoSQL-Antoine Nguyen cao/movies_rated_tagged.json", 'r') as fic:

    #data=fic.read()
#print (data)

#with open("C:/Users/Antoine/Documents/Repo_NoSQL-Antoine Nguyen cao/movies_rated_tagged.json", 'r') as fic:
    #data_dict = json.load(fic)
    #print(data_dict)

#with open("C:/Users/Antoine/Documents/Repo_NoSQL-Antoine Nguyen cao/movies_rated_tagged.json", 'r') as fic:
    #data_dict = json.load(fic)

#data_str = json.dumps(data_dict)
#print(data_str)



    #import pandas as pd

#fichier = pd.read_json (r'C:/Users/Antoine/Documents/Repo_NoSQL-Antoine Nguyen cao/movies_rated_tagged.json')
#print (fichier)


#df = pd.DataFrame(fichier, columns= ['movieId','tag'])
#print (df)

#import numpy as np
#import pandas as pd

#fichier = pd.read_json (r'C:/Users/Antoine/Documents/Repo_NoSQL-Antoine Nguyen cao/movies_rated_tagged.json')

#df3 = pd.DataFrame(np.arange(1,100,0.12).reshape(33,25))

#fichier.describe()

import pandas as pd
from py2neo import Graph, Relationship, Node


df = pd.read_json("C:/Users/A.NGUYENCAO/Documents/movies_rated_tagged.json")
print (df)

df.drop(df.columns[[0, 1, 24, 25, 26, 27, 28, 29, 30]], axis=1, inplace=True)

graph = Graph("http://localhost:7474/")

titre = Node(name="Title")
genre = Node(name="Genres")
tg = Relationship(titre, "Relations", genre)
graph.create(tg)

annee = Node(name="year")
genre = Node(name="Genres")
ag = Relationship(annee, "Relations", genre)
graph.create(ag)

from py2neo import Graph
from py2neo.matching import *
    graph = Graph()
    nodes = NodeMatcher(g)
    tag = nodes.match("tag", name="pixar").first()pixar
tag = Node(name='tag')



