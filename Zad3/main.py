fib1 = 1
fib2 = 1
i = 0
for n in range (1,22):
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    print("Четырехзначный элемент",fib2, 1000<fib2<10000)
print('Всего элементов 4')
