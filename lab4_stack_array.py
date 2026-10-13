# LAB ASSIGNMENT 4
# Q1: Stack Using Static Array

MAX = 5
stack = [None] * MAX
top = -1

def push(value):
    global top

    if top == MAX - 1:
        print("Stack Overflow")
    else:
        top += 1
        stack[top] = value
        print("Element Pushed:", value)

def pop():
    global top

    if top == -1:
        print("Stack Underflow")
    else:
        print("Element Popped:", stack[top])
        stack[top] = None
        top -= 1

def display():
    if top == -1:
        print("Stack is Empty")
    else:
        print("Stack:", stack[:top + 1])


while True:
    print("\n--- STACK USING ARRAY ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        value = int(input("Enter Value: "))
        push(value)

    elif choice == 2:
        pop()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")