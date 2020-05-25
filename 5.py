#sum of elements in a list:
list=[1,2,3,4,5,6,7,8,9]
a=sum(list)
print(a)
"or"
#from user inputs:
print('Enter the numbers into list:')
list=[]
while len(list)<10:
    a=int(input())
    list.append(a)
print('Sum of elements in list:', sum(list))
