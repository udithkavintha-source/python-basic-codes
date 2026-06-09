def greeting(name,age):
    '''this function depects name and age'''
    a='Hi' ,name, 'Your age is' ,age
    z=' '.join(a)
    return z  
b=input('Enter name ')
c=input('Enter age  ')
print(greeting(b,c))