# Reverse a list in a circular way:
x=[1,2,3,4,5,6,7,8,9]
x.reverse()
print(x)
#OR
x=[1,2,3,4,5,6,7,8,9,10]
for i in x[::-1]:
    print (i,end=',')
