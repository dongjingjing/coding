#求和
price_list = [34, 10, 23, 53, 12, 45, 12, 34, 10, 78, 34, 1, 3, 5, 90,90, 23, 5, 77, 83, 44, 59]
sum=0
for item in price_list:
		sum=sum+item
print(sum)

#求平均数
a=len(price_list)
mean=sum/a
print(mean)

#找出最大值
max=price_list[0]
for item in price_list:
	if item >max:
		max=item
print(max)

##second_price_list=price_list.remove(max_price)
##print(price_list)
#not so good ,did not consider there may be more than two max
s_price_list=[]
for item in price_list:
	if item != max:
		s_price_list.append(item)
print(s_price_list)


#编辑求和函数
def mymax(l):
	if len(l)==0:
		return None
	else:
		max=l[0]
		for item in l:
			if item>max:
				max=item
		return max
	



l=[34, 10, 23, 53, 12, 45, 12, 34, 10, 78]
print(mymax(l))

#寻找交集
def myintersection(l1,l2):
	l=[]
	for item1 in l1:
		for item2 in l2:
			if item2 in l:
				pass
			else:
				if item1==item2:
					l.append(item2)
	return(l)
l1=[1,2,3,4,4]
l2=[1,3,3,4,5,4]
print(myintersection(l2,l1))

#形成一个library：
l = ['apple', 'pear', 'orange', 'apple', 'orange', 'orange', 'apple', 'pear']
d={}
for item in l:
	if item in d:
		d[item]=d[item]+1
	else:
		d[item]=1
print(d)


#根据library形成一个list

s={'pear': 2, 'orange': 4, 'apple': 5}
l=[]

for key in s:
	i=0
	while i < s[key]:
		i+=1
		l.append(key)
print(l)

#产生#阵：
m=5
for i in range(0,m):
	for j in range(0,m-i):
		print(' ',end='')
	for j in range(0,2*i+1):
		print('#',end='')
	print('')

import random
#设计一个抽奖模式：答对则结束，打错则继续答题
x=int(input('plese enter an integer(0-1000):'))
a=random.randint(0,1000)
while x != a:
	if x>a:
		print('it is too big')
	if x<a:
		print('it is too small')
	x=int(input('plese enter an integer(0-1000):'))
print('congratulations')
