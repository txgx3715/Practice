#问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
#则输出为:40320
def fact(x):
    if x == 0 or x == 1:
        return 1
    return (x*fact(x-1))
x = eval(input("请输入数字："))
print(fact(x))



