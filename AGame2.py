num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))
def max(num1,num2,num3):
    if num1 >= num2 & num1 >= num3 :
        return num1
    elif num2 >= num1 & num2 >= num3 :
        return num2
    else :
        return num3
print(max(num1,num2,num3))