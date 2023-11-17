expression = input("Please enter an expression (num1, space, num2 ")
num1, sign, num2 = expression.split(" ")
num1 = int(num1)
num2 = int(num2)
if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    print(num1 / num2)
else:
    print("Unknown Expression")