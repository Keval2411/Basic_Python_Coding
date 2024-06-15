dict1 = {575:'Apple' , 876:'Graps' , 989:'Mango' , 243:'Banana'}

d = sorted(dict1.keys())
dict2 = {}
for i in d :
    dict2[i] = dict1[i]
    
print(dict2)

#By Value

dict1 = {575:'Apple' , 876:'Graps' , 989:'Mango' , 243:'Banana'}

dict2 = {key : value for key , value in sorted(dict1.items(), key=lambda x: x[1])}

print(dict2)