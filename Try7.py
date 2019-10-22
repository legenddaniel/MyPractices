'''
三个单引号内的区域等同#，但是是斜体字
'''
# 如果写#就要每行写一个

print()
try: #只能显示第一个错误 r w a r+
    answer = 10/0
    num = int("dog")
    print(num)
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2:
    print(err2)

print()
num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "^":
    print(num1 ** num2)
else:
    print("Invalid operator")