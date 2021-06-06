import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

ls = []
for _ in range(100):
    ls.append(random.randint(1, 500))
print(bubble_sort(ls))
