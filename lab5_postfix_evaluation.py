# LAB ASSIGNMENT 5
# Q2: Postfix Expression Evaluation

def evaluate_postfix(expression):
    stack = []

    for ch in expression:

        if ch.isdigit():
            stack.append(int(ch))

        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)

            elif ch == '-':
                stack.append(a - b)

            elif ch == '*':
                stack.append(a * b)

            elif ch == '/':
                stack.append(a / b)

            elif ch == '^':
                stack.append(a ** b)

    return stack.pop()


expression = input("Enter Postfix Expression: ")

result = evaluate_postfix(expression)

print("Result:", result)