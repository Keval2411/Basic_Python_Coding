def prime_num(n):
    flag = False
    if n>1:
        for i in range(2,n):
            if n%i ==0:
                flag = True
                break
        if flag:
            return("no, it's not a prime number")
        else:
            return("yes, it's a prime number")
print(prime_num(23))

#start end

def prime_num1(start,end):
    for n in range(start,end):
        if n>1:
            for i in range(2, n//2+1):
                if n%i==0:
                    break
            else:
                print(n)
prime_num1(20,100)