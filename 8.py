# smallest and largest number in the list:
a=[1,2,3,4,5,6,7,8,9,10]
print('Maximum number:',max(a))
print('Minimum number:',min(a))
#from user input:
print('Enter the numbers:')
list=[]
while len(list)<10:
    a=int(input())
    list.append(a)
print('max num:',max(list))
print('min num:',min(list))
#or
'''we can sort the list and find the max and min numbers'''
list.sort()
print('sorted list:',list)
print('max number:',list[-1])
print('min number:',list[0])
