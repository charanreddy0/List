#Adding Matrixes:
x=[  [1,2,3],
       [4,5,6],
       [7,8,9]  ]
y=[  [1,2,3],
       [4,5,6],
       [7,8,9] ]
z=[  [0,0,0],
        [0,0,0],
        [0,0,0] ]
for i in range(len(x)):
    for j in range(len(x[0])):
        z[i][j]=x[i][j]+y[i][j]
print(z[0],'\n')
print(z[1],'\n')
print(z[2],'\n')
