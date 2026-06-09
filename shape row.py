#input or furet     argument is number of rows
a=int(input('Enter number  '))
for i in range(1,a+1):
    print(str('*'*i))

for i in range(a,0,-1):
    print(str('*'*i))