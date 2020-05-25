'''Splitting evens in one list and odds in one list'''
a=[1,2,3,4,5,6,7,8,9]
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)
'''splitting list into middle and stored in two lists'''
b=[5,2,577,35,45,355.654,2468.2288,3354,'charan','hcl','python',855.98,6685]
half=(len(b)//2)
print('First Half list:',b[:half])
print('Second half list:',b[half:])
