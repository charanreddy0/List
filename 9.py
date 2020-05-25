a=[1,2,3,4,5,6,7,8,9,10]
#using for loop:
sum=0
for i in a:
    sum=sum+i
print('sum of elements:',sum)
print('average of elements:',sum/len(a))
print('max num',max(a))
print('min num',min(a))
# using while loop
add=0
count=0
while count<len(a):
    add=add+a[count]
    count+=1
print(add)
print('avg:', add/count,'or',add/len(a))
print('max:',max(a))
print("min:", min(a))
