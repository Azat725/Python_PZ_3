a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

for i in range(a, b + 1):
    if(i % 2):
        print(i)