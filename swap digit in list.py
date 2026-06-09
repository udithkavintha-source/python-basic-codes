a=list(input('Enter your number'))
y=a[0]
x=a[-1]
a[0]=x
a[-1]=y
p="".join(a)
print(p)