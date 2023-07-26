from random import randint
n = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n)
m = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(m)

c = n.intersection(m)
print(c)