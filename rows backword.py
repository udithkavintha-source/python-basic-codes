a=int(input('Enter number   '))
p=1
while p<=a:
    for i in range(a,0,-1):
        print(' '*i,"*"*p)
        p=p+1