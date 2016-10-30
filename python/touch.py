import csv
import matplotlib.pyplot as plt

l=[]
d={}
t1 = 0
t2 = 0
u1 = 0
with open('tbl_user.csv','r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
    	if row[2].strip():
    		print(row[2])
    		u1 += 1

    	email = row[3].strip()
    	t1 += 1
    	if email:
    		t2 += 2
    		x=email.index('@')
    		y=email.index('.',x)
    		company = email[x+1:y]
    		l.append(company)
    	# l=[]
    	# if company not in l:
    	# 	l.append(company)

    for item in l:
    	if item in d:
    		d[item]=d[item]+1
    	else:
    		d[item]=1

# Data to plot
labels = list(d.keys())
sizes = list(d.values())
plt.pie(sizes, labels=labels)
# labels = 'Python', 'C++', 'Ruby', 'Java'
# sizes = [215, 130, 245, 1000]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# # Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()

# print(d)
print(t1)
print(u1)