import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

sizes = [10000, 50000, 100000]

for n in sizes:
    arr = list(range(n))
    target = n - 1

    start = time.perf_counter()

    result = linear_search(arr, target)

    end = time.perf_counter()

    execution_time = (end - start) * 1000000

    print("Array Size:", n)
    print("Target Found at Index:", result)
    print("Execution Time:", round(execution_time, 2), "microseconds")
    print()