a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a > b:
    for i in range(b, a + 1):
        if(i % 2):
            print(i)

else:
    for i in range(a, b + 1):
        if(i % 2):
            print(i)