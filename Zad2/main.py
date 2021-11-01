n=int(input('Сколько будет слагаемых: '))
a=1
l=3
for i in range(n-1):
    if i%2==0:
        a=a-1/l
    else:
        a=a+1/l
    l+=2
print('Приближенное значение ПИ будет равно:',a*4)
