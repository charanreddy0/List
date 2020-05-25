'''Take 10 inputs from user and delete repeted elements:'''
print("Enter the numbers:")
a=[]
i=0
while len(a)<10:
    b=int(input())
    a.append(b)
print(a)
c=[]
for i in a:
    if i not in c:
        c.append(i)
print(c)
    
