# LAB ASSIGNMENT 2
# Basic Array Operations

arr = []

while True:
    print("\n--- ARRAY OPERATIONS ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        pos = int(input("Enter index: "))

        if 0 <= pos <= len(arr):
            arr.append(0)

            for i in range(len(arr) - 1, pos, -1):
                arr[i] = arr[i - 1]

            arr[pos] = value
            print("Element Inserted Successfully")

        else:
            print("Invalid Index")

    elif choice == 2:
        pos = int(input("Enter index to delete: "))

        if 0 <= pos < len(arr):
            for i in range(pos, len(arr) - 1):
                arr[i] = arr[i + 1]

            arr.pop()
            print("Element Deleted Successfully")

        else:
            print("Invalid Index")

    elif choice == 3:
        value = int(input("Enter element to search: "))
        found = -1

        for i in range(len(arr)):
            if arr[i] == value:
                found = i
                break

        if found != -1:
            print("Element Found at Index:", found)
        else:
            print("Element Not Found")

    elif choice == 4:
        print("Array:", arr)

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
        