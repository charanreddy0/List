# 10 inputs from user and store reverse order in another list
print('Enter the numbers:')
a=[]
while len(a)<10:
    b=int(input())
    a.append(b)
print("List before in reverse order:")
print(a)
a.sort()
a.reverse()
b=a.copy()
print('List in reverse order:')
print(b)
