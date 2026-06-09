a=int(input('Enter number   '))
p=1
c=1
for i in range(a,0,-1):
    if c%2==0:
        print('   '*i,' $ '*p)
        p=p+2 
        c=c+1
    else:
        print('   '*i,' * '*p)
        p=p+2 
        c=c+1