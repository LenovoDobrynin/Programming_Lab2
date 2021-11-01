try:
    N = int(input("Введите целое число N в интервале [1;100]: "))
except ValueError:
        print('Нужно ввести цифру')
else:
    if N < 0:
        print("Ошибка! Вводите только положительные числа")
    elif N >100:
        print('Написано же, от 1 до 100')
    else:
        A = str(N)
        if N >= 10 and N <= 20:
            print(A + " лет")
        elif A.endswith('1') is True:
            print(A + " год")
        elif A.endswith('2') is True \
        or A.endswith('3') is True \
        or A.endswith('4') is True:
            print(A + " года")
        else:
            print(A + " лет")
