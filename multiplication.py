def multiplication(num1,num2=12):
    for i in range(1,num2+1):
        tot=num1*i
        print(f"{num1}*{i}={tot}")
a=int(input('Enter num 1    '))
b=int(input('Enter num2     '))
multiplication(a,b)