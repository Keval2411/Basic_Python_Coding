def Nth_Highest_Num(l,n):
    l.sort(reverse=True)
    print(l)
    print(l[n-1])
    
l = [10,30,50,100,75,200]
Nth_Highest_Num(l,2)
    