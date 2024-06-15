k = 'inikkgevalltppghhvvdd'
ch = {}

for i in k:
    if i in ch:
        ch[i] += 1
    else :
        ch[i]= 1

max_char = max(ch, key =ch.get)
print(max_char)

# Find the max and min value frome a list

l = [0,1,4,24,43,100,475]
maximum = l[0]
minimum = l[0]

for i in l :
    if i> maximum :
        maximum = i
    if i< minimum :
        minimum = i
        
print('maximum : ', maximum)
print('minimum : ', minimum)