# LAB SHEET 9
# Q3: Searching and Sorting Comparison

import time
import random


# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search
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


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Bucket Sort
def bucket_sort(arr):
    if not arr:
        return arr

    n = len(arr)
    buckets = [[] for _ in range(n)]

    minimum = min(arr)
    maximum = max(arr)

    if minimum == maximum:
        return arr

    for value in arr:
        index = int(
            (value - minimum) * (n - 1) /
            (maximum - minimum)
        )
        buckets[index].append(value)

    result = []

    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)

    return result


# Execution Time Measurement
def measure_time(func, arr):
    data = arr.copy()

    start = time.perf_counter()

    result = func(data)

    end = time.perf_counter()

    assert result == sorted(arr)

    return (end - start) * 1000


# Main Program
n = int(input("Enter array size: "))

random.seed(42)
arr = [random.randint(1, 10000) for _ in range(n)]

print("\nArray Size:", n)

algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort),
    ("Bucket Sort", bucket_sort)
]

print("\n--- SORTING EXECUTION TIMES ---")

for name, function in algorithms:
    execution_time = measure_time(function, arr)

    print(
        name, ":",
        round(execution_time, 4),
        "milliseconds"
    )


# Searching Comparison
sorted_arr = sorted(arr)
target = sorted_arr[-1]

print("\n--- SEARCHING EXECUTION TIMES ---")

start = time.perf_counter()
linear_result = linear_search(sorted_arr, target)
end = time.perf_counter()

linear_time = (end - start) * 1000000

print("Linear Search Index:", linear_result)
print("Linear Search Time:",
      round(linear_time, 4), "microseconds")


start = time.perf_counter()
binary_result = binary_search(sorted_arr, target)
end = time.perf_counter()

binary_time = (end - start) * 1000000

print("Binary Search Index:", binary_result)
print("Binary Search Time:",
      round(binary_time, 4), "microseconds")