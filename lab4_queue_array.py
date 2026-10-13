# LAB ASSIGNMENT 4
# Q3: Queue Using Static Array

MAX = 5
queue = [None] * MAX
front = 0
rear = -1

def enqueue(value):
    global rear

    if rear == MAX - 1:
        print("Queue Overflow")
    else:
        rear += 1
        queue[rear] = value
        print("Element Inserted:", value)

def dequeue():
    global front, rear

    if front > rear:
        print("Queue Underflow")
    else:
        print("Element Deleted:", queue[front])
        queue[front] = None
        front += 1

        if front > rear:
            front = 0
            rear = -1

def display():
    if front > rear:
        print("Queue is Empty")
    else:
        print("Queue:", queue[front:rear + 1])


while True:
    print("\n--- QUEUE USING ARRAY ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        value = int(input("Enter Value: "))
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")