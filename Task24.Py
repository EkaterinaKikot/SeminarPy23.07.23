import random
k = int(input("Введите количество кустов: "))
b = list(random.randint(0, 10) for i in range(k))
result = []
i = 0
sum = 0

print(b)

while (i < k):
    if (i == k - 1):
        sum = b[i] + b[i - 1] + b[0]
    else:
        sum = b[i] + b[i - 1] + b[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(f"Максимальное число ягод за одну итерацию {result[-1]}")