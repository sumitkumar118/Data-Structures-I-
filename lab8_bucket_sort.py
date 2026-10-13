# LAB SHEET 8
# Q4(B): Bucket Sort

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    n = len(arr)

    buckets = [[] for _ in range(n)]

    min_value = min(arr)
    max_value = max(arr)

    if min_value == max_value:
        return arr

    for value in arr:
        index = int(
            (value - min_value) * (n - 1) /
            (max_value - min_value)
        )

        buckets[index].append(value)

    result = []

    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)

    return result


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

print("Original Array:", arr)

sorted_arr = bucket_sort(arr)

print("Sorted Array:", sorted_arr)