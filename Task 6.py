import random

array = [random.randint(-100, 100) for _ in range(10)]
for i in range(len(array)):
    array[i] *= -1