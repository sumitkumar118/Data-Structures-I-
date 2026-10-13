# LAB SHEET 8
# Q4(A): Insertion Sort

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

print("Original Array:", arr)

insertion_sort(arr)

print("Sorted Array:", arr)