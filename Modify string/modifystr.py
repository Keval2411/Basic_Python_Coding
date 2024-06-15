def str_format(s):
    l = []
    temp = s.split('_')
    for i in temp :
        l.append(i[0].lower() + i[1:].upper())
    s = '.'.join(l)
    print(s)
    
s= 'This_Is_a_Gods_Plan'
str_format(s)