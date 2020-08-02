print("Welcome to building a calculator:\nInput you number and operator.")

num1 = float(input("Enter you number 1: "))
op = input("Enter you oprator :")
num2 = float(input("Enter you number 2 :"))
from math import *

if op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "%":
    print(num1 % num2)
elif op == "round":
        print(round(num1))
elif op == "sqrt":
        print(sqrt(num1))
elif op == "floor":
        print(floor(num1))
elif op == "ceil":
        print(ceil(num1))
else :
    print("Invalid oprator")
    