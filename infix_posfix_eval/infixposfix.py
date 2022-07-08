from stack import *


def postfix(infix):
    stack = Stack()
    postfix = []

    for i in range(len(infix)):
        element = infix[i]
        if '0' <= element <= '9' or 'a' <= element.lower() <= 'z':
            postfix.append(element)
        elif isOperator(element):
            while not (stack.isEmpty() or not priority(element, stack.stacktop())):
                unstack = stack.pop()
                postfix.append(unstack)
            stack.push(element)
        elif element == '(':
            stack.push(element)
        elif element == ')':
            while True:
                top = stack.pop()
                if top != '(':
                    postfix.append(top)
                else:
                    break
    while not stack.isEmpty():
        postfix.append(stack.pop())

    postfix = "".join(postfix)

    return postfix


def operation(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op2 - op1
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op2 / op1
    else:
        return False  # Retorna False caso o operando não seja válido


def eval_Posfixa(expression):
    stack = Stack()
    for i in range(len(expression)):
        element = expression[i]
        if "0" <= element <= "9":
            stack.push(element)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            value = operation(element, int(operand1), int(operand2))

            if value:
                stack.push(value)
            else:
                return "Invalid Operator!"

    result = stack.pop()

    if stack.isEmpty():
        return result
    else:
        return "Wrong Expression!!"


def isOperator(simb):
    if simb == "+" or simb == "-" or simb == "*" or simb == "/":
        return True
    else:
        return False


def priority(op_1, op_2):
    if op_1 == "+" or op_1 == "-":
        operator_1 = 1
    elif op_1 == "*" or op_1 == "/":
        operator_1 = 2
    else:
        operator_1 = 3
    if op_2 == "+" or op_2 == "-":
        operator_2 = 1
    elif op_2 == "*" or op_2 == "/":
        operator_2 = 2
    else:
        operator_2 = 0
    return operator_1 <= operator_2


def evaluate(postfix):
    global num1, num2
    stack = Stack()

    for i in range(len(postfix)):
        element = postfix[i]
        if "0" <= element <= "9":
            stack.push(element)
        else:
            try:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
            except AttributeError:
                print("There is a spare operator in expression!!!")
                exit()
            result = operation(element, num1, num2)

            if result:
                stack.push(result)
            else:
                return "Invalid Operator!!"
    final = stack.pop()
    if stack.isEmpty():
        return final
    else:
        return "Invalid Expression !!"
