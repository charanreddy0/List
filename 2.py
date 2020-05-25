# 10 input numbers in list and compare the 11th num in list to store or not. 
print('Enter the Numbers:')
a=[]
while len(a)<10:
    b=int(input())
    a.append(b)
print(a)
c=int(input('Enter a one number again:'))

if c in a:
     print("this number already in a list:")
else:
    a.append(c)
    print("just before u entered a number is not in a list previosly:")
    print('new list:',a)
