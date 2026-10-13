# LAB ASSIGNMENT 5
# Q1: Infix to Postfix Conversion

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:

        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   (precedence(stack[-1]) > precedence(ch) or
                   (precedence(stack[-1]) == precedence(ch)
                    and ch != '^'))):
                postfix += stack.pop()

            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix


expression = input("Enter Infix Expression: ")

result = infix_to_postfix(expression)

print("Postfix Expression:", result)
