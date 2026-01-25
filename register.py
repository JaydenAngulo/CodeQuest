sum = 0

for i in range(1, 573000):
    if i % 2 == 1:
        sum += i ** 2

print(sum)