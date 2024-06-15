k = 'kevek'
if k == k[::-1] :
    print('yes, It is palindrome')
else :
    print('No, It is not palindrome ')
    
# Alternative way

K = 'Keval'
n= len(K)
x=0

for i in range(n) :
    if K[i] != K[n-i-1] :
        x=1
        break
if x==0 :
    print('yes pelindrome')
else :
    print('NO')
    
#By using while loop

def pelindrome(s):
    n = len(s)
    first = 0
    last = n-1
    
    while (first<last):
        if s[first] == s[last]:
            first += 1;
            last  -= 1;
        else:
            return False
    return True

s = input("Enter a string:")
pelindrome(s)
print(pelindrome(s))
