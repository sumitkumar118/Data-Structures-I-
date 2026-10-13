import time

def nested_loops(n):
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    return count

sizes = [100, 500, 1000]

for n in sizes:

    start = time.perf_counter()

    result = nested_loops(n)

    end = time.perf_counter()

    execution_time = (end - start) * 1000000

    print("Input Size:", n)
    print("Total Operations:", result)
    print("Execution Time:", round(execution_time, 2), "microseconds")
    print()