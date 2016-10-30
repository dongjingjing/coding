import random

##price_list = [34, 10, 23, 53, 12, 45, 12, 34, 10, 78, 34, 1, 3, 5, 90, 23, 5, 77, 83, 44, 59]
##
##sum_price = 0
##
##for price in price_list:
##    sum_price = sum_price + price;
##a=len(price_list)
##mean=sum_price/a
##var_sum_price=0
##for price in price_list:
##    var_sum_price = var_sum_price + (price - mean )*(price - mean )
###print(var_sum_price)
##
##
###print("hello world")
##
###mystring="hello world"
###print("mystring")
##
##max_price =price_list[0]
##for price in price_list:
##    if price >max_price:
##        max_price= price
##second_price_list=price_list.remove(max_price)
##print(price_list)
##
###print(max_price)
##
##
##second_max_price =price_list[0]
##for price in price_list:
##    if price >max_price:
##        second_max_price= price
##print(second_max_price)
##
##
##print(sum(price_list))


##def mysum(l):
##   s = 0
##    for item in l:
##        s += item
##   return s
##
##
#def mymaxandremove(l):
#   if len(l) == 0:
#        return None
#    max_l=l[0]
#  for item in l:
#       if item>max_l:
#         max_l=item

#  l.remove(max_l);
# return max_l
# #
# def mymax(l):
# if len(l) == 0:
#     return None
# max_l=l[0]
#  for item in l:
#       if item>max_l:
#            max_l=item
#   return max_l
# #
##print(sorted(price_list)[10])
##
##i=0
##while i<9:
##    i+=1
##    mymaxandremove(price_list)
##
##print(mymaxandremove(price_list))
##  
##
##def intersection(l1,l2):
##    l=[]
##    for item1 in l1:
##        for item2 in l2:
##            if item2 in l:
##                pass
##            else:
##                if item1==item2:
##                    l.append(item2)
##    return l
##
##l1=[1,2,3,3,4]
##l2=[2,3,4]
##l = intersection(l1,l2)
##print(l)
##
##d={ 'name':'djj','gender':'f'}
##print(d['name'])
##
##
##l=[{'name':'djj','gender':'f'},{'name':'xwb','gender':'m'}]
##print(l[0]['name'])
##
##d={
##    'address':{'city':'hangzhou','province':'zhejiang'},
##               'name':{'first':'jj','second':'d'}
##               }
##print(d['address']['city'])



# l = ['apple', 'pear', 'orange', 'apple', 'orange', 'orange', 'apple', 'pear']
# d={}
# for item in l :
#     if item in d :
#         d[item]=d[item]+1
#     else:
#         d[item]=1
# ##print(d)
##f_l=[]
##for key in d:
##    i=0
##    while i < d[key]:
##        i+=1
##        f_l.append(key)
##print(f_l)
##


    

##m = 3
##for i in range(1, m):
##    for j in range(0, m-i):
##        print(' ', end='')
##    for j in range(0, i*2):
##        print('#', end='')
##    print('')


##g_h=[1.4,1.5,1.7,1.8,1.9,1.5,1.6,1.7,1.3,1.4,1.8]
##b_h=[1.7,1.6,1.8,1.9,1.6,1.8,1.9,1.6,1.5,1.7,1.6]
##i=0
##for item1 in g_h:
##    for item2 in b_h:     
##        if item1>item2:
##            i+=1
##print(i)
##
##d={}
##for item in g_h:
##    if item in d:
##        d[item]=d[item]+1
##    else:
##        d[item]=1
##print(d)
##g_h_l=[]
##for key in d:
##    i=0
##    while i<d[key]:
##        i+=1
##        g_h_l.append(key)
##print(g_h_l)
##g_h_l.sort(key=None,reverse=True)
##print(g_h_l)
##
##


##while true:
##    # print one line
##    for a
##        print(' ', end='')
##    for b
##        print('#', end='')
##    print('')
####
##
##l = [3,2,3]
##for item in l:
##    print(item)
##
##for i in range(0, len(l),2):
##    print(l[i])



m=3
for i in range(0,m):
    for j in range(0,m-i):
        print(' ',end='')
    for j in range(0,2*i+1):
        print('#',end='')
    print('')


x=int(input('please enter an integer[1-1000]:'))
a=random.randint(1, 1000)
while x!=a:
    if x>a:
        print('It is too big')
    if x<a:
        print('It is too small')
    x=int(input('please enter an integer[1-1000]:'))

print('congratulations!')
print(x)
            
x=1

