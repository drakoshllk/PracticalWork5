import random

arr = [random.randint(-100, 100) for _ in range(10)]
for i in range(len(arr)):
    arr[i] *= -1