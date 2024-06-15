K = 'sky is the blue'
l = K.split()
l = l[::-1]
l = ' '.join(l)
print(l)

#Remove Punctuation

str1 = '/*apples are & found % only @ red & green'
s= ''

for i in str1:
    if((i>='A' and i<='Z') | (i>='a' and i<='z') | (i == ' ')) :
        s = s+i
        
print(s)
