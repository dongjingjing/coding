l = ['apple', 'pear', 'orange', 'apple', 'orange', 'orange', 'apple', 'pear']
d={}

for item in l:
    if item in d:
        d[item]=d[item]+1
    else:
        d[item]=1

fruit_list=[]

for key in d:
    i=0
    while i<d[key]:   
        i += 1
        fruit_list.append(key)

print(fruit_list)
d={}
for item in l :
    if item in d :
        d[item]=d[item]+1
    else:
        d[item]=1
f_l=[]
for key in d:
    i=0

    while i<d[key]:
        i += 1
        f_l.append(key)
    
print(f_l)



    
    

