print('enter a number:')
a=[]
while len(a)<5:
    b=int(input())
    a.append(b)
print(a)
even_count=0;odd_count=0;zero_count=0;positive_count=0;negetive_count=0
num=0
while (num<len(a)):
    if a[num]%2==0:
        even_count+=1
    if a[num]%2!=0:
        odd_count+=1
    if a[num]==0:
        zero_count+=1
    if a[num]>=0:
        positive_count+=1
    else:
        negetive_count+=1
    num+=1
print('even:',even_count)
print('odd:',odd_count)
print('zeros:',zero_count)
print("positive numbers:", positive_count)
print("negetive numbers:", negetive_count)


