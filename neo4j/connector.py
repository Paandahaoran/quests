# coding=utf-8
import os
import json
#F:\JR_data\new_data
with open(os.path.join('/Users/paanda/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-94abfa63-97b2-4e1b-9b52-b8cd02797980/installation-3.5.14/import/', 'review.json'), 'r') as f1:
    ll = [json.loads(line.strip()) for line in f1.readlines()]
    total = len(ll)//100
    for i in range(0,2):
        json.dump(ll[i*100:(i+1)*100], open("/Users/paanda/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-94abfa63-97b2-4e1b-9b52-b8cd02797980/installation-3.5.14/import/" + str(i) + ".json", 'w'), ensure_ascii=False, indent=True)
