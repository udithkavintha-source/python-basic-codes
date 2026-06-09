a=int(input('Enter your number  '))
prev=0
next=1
i=0
if i==a:
    print(prev)
else:
    if a==1:
        print(next)
    else:
        i=2
        while i<a:
            temp=prev+next
            prev=next
            next=temp
            i=i+1
        print(temp)