'''Multiplication of matrix:'''
a=[[1,1,1],[2,2,2],[3,3,3]]
b=[[1,1,1],[2,2,2],[3,3,3]]
c=0
d=[]
for i in a:
    for j in i:
        for x in b:
            for y in x:
                d=a[i][j]+b[i][j]
print(d)
