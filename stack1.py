from collections import deque

def precedence(i):
    if i == '*' or i == '/':
        return 2
    elif i == '+' or i == '-':
        return 1
    else:
        return 0

def infixtopostfix(infix):
    stack = deque()
    postfix = ""
    for i in infix:
        if i.isdigit():
            postfix += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(i):
                postfix += stack.pop()
            stack.append(i)
    while stack:
        postfix += stack.pop()
    return postfix

def operate(a, b, i):
    if i == "+":
        return b + a
    elif i == "-":
        return b - a
    elif i == "*":
        return b * a
    elif i == "/":
        return b // a  # integer division

def postevaluation(expr):
    stack = deque()
    for i in expr:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(operate(a, b, i))
    return stack.pop()

# Example usage
infix_expr = "2+5-(6*9)+2"
postfix_expr = infixtopostfix(infix_expr)
result = postevaluation(postfix_expr)
print(postfix_expr)
print(result)
