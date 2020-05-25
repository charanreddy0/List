#Is list same if we read from either from front or back:
a=[1,2,3,4,5,4,3,2,1]
if a[:]==a[::-1]:
    print("list is same",a)
else:
    print("not same",a)
b=[1,2,3,4,5,6,7,8,9]
if b[:]==b[::-1]:
    print("list is same",b)
else:
    print("not same",b)
