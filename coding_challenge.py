# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 16:55:25 2016

@author: Aqeel Awais
"""
#parse json file line by line
import json
#f=open("products.txt","r")
#s=f.read()
#product=json.loads(s)

#products Data
data = []
with open('products.txt') as f:
    for line in f:
        data.append(json.loads(line))

#all models with product names
        
all_models=[]
for element in data:
    all_models.append(element['model'])
#all manufacturers in products
    
all_manuf=[]
for element_1 in data:
    all_manuf.append(element_1['manufacturer'])

all_prod=[]
for element_3 in data:
    all_prod.append(element_3['product_name'])
#family not considered because some of the products are without family names
#all_family=[]
#for element_5 in data:
#    all_family.append(element_5['family'])

#listings Data
data_listings = []
#with open('listings.txt',encoding="utf8") as f_1: #windows
with open('listings.txt') as f_1:  #Linux
    for line_2 in f_1:
        data_listings.append(json.loads(line_2))
#listngs Manufacturers
all_list_manu=[]
for element_2 in data_listings:
    all_list_manu.append(element_2['manufacturer'])
#listing title
all_list_title=[]
for element_4 in data_listings:
    all_list_title.append(element_4['title'])
    
#################################################
compl_dic=dict()
for i in range(0,len(data)):
    for j in range(0,len(data_listings)):
        #check manufacturer
        if all_manuf[i]==all_list_manu[j]:
           #print(all_manuf)
        
           str_1=all_list_title[j]
           str_2=all_models[i]
           #check model
           if str_1.find(str_2) != -1:
               #check family if any family key exists in dic and it corresponds to price listings 
              if any('family' in d for d in data[i])==True:
                   str_3=data[i]
                   str_4=str_3['family']
                   if str_4.find(str_1) !=-1:    
                       if all_prod[i] in compl_dic:
                           compl_dic[all_prod[i]].append(data_listings[j])
                       else:
                           compl_dic[all_prod[i]]=[data_listings[j]]
              #if family does not exist                 
              else:
                  if all_prod[i] in compl_dic:
                           compl_dic[all_prod[i]].append(data_listings[j])
                  else:
                           compl_dic[all_prod[i]]=[data_listings[j]]
               
             
                   
              #compl_dic[all_prod[i]]=data_listings[j]
              
#print(compl_dic)
with open('result.txt', 'w') as fp:
    json.dump(compl_dic, fp, indent=2)
    #fp.write('\n')

#if any('family' in d for d in data[0])==True:
#    str_3=data[0]
#    print(str_3['family'])
               
