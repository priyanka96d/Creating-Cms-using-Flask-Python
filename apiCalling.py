import requests
import json

from requests import api

apiData = []
res = requests.get("https://fakestoreapi.com/products")
data = res.json() 
id = [] 
title = []
price = []
category = []
desc = []
image=[]

for i in range(len(data)):
    id.append(data[i]["id"])
    title.append(data[i]["title"])
    price.append(data[i]["price"])
    category.append(data[i]["category"])
    desc.append(data[i]["description"])
    image.append(data[i]["image"])
 




"""
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    
jprint(res.json())


 

for i in range(len(data)):
    for key,value in data[i].items():   
        print(i.get("id"))
        print("--------")
        print()
 
id = []
for i in range(len(data)):
    for key in data[i].items: 
        id.append(data[key].get("id"))

print(id)
 """  

