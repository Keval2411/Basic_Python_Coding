list1 = [43,7,18,24,17,9,37,11]
n = len(list1)

for i in range(n):
    for j in range(i+1,n):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j] , list1[i]
            
print(list1)