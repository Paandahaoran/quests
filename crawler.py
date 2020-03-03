import json

file = open('test.json','r',encoding='utf-8')
s = json.load(file)
print (s['name'])
file.close()
