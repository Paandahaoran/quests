# -*- coding: utf-8 -*-
from py2neo import Graph
import json
#json dict file
with open("test.json",'r') as load_f:
    load_dict = json.load(load_f)
#neo4j graph connect
 graph = Graph("http://localhost:7474", username="neo4j", password='panda')

#build query
query=""


 graph.create(s)
