# 画出#键
m=3
for i in range(0,3):
	for j in range(0,m-i):
		print(' ',end='')
	for j in range(0,2*i+1):
		print('#',end='')
	print('')


