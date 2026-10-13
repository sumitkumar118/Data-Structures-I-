import time

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

sizes = [10000, 50000, 100000]

for n in sizes:
    arr = list(range(n))
    target = n - 1

    start = time.perf_counter()

    result = binary_search(arr, target)

    end = time.perf_counter()

    execution_time = (end - start) * 1000000

    print("Array Size:", n)
    print("Target Found at Index:", result)
    print("Execution Time:", round(execution_time, 2), "microseconds")
    print()