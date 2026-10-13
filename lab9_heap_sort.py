# LAB SHEET 9
# Q2: Heap Sort

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print("Max Heap:", arr)

    # Extract Root Repeatedly
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

print("Original Array:", arr)

heap_sort(arr)

print("Sorted Array:", arr)