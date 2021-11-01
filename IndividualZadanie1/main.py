try:
    x = float(input('Введите первое вещественное число: '))
    y = float(input('Введите второе вещественное число: '))
    z = float(input('Введите третье вещественное число: '))
except:
    print('Ошибка в ведении числа')
else:
    f = [x,y,z]
    t = max(f)
    n = min(f)
    d =sum(f)
    h= d - t
    m = d - (t+n)
    u = m*n
    print(u)

