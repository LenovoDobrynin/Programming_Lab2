try:
    N=int(input('Введите натуральное число N: '))
except:
    print('Ошибка в ведении числа')
else:
    k=0
    for x in range(N):
        if(x**3>N):
            break
        for y in range(N):
            if(y**3+x**3>N):
                break
            for z in range(N):
                if(y**3+x**3+z**3>N):
                    break
                if((x**3)+(y**3)+(z**3)==N):
                    print(x,y,z)
                    k+=1
    if(k==0):
        print('No such combinations')