#获得用户的非数字输入， 如果输入中存在数字， 则要求用户重新输入， 直至满足条件为止， 并输出用户
#输入字符的个数， 完善PY202 ． 文件中的代码。


while True:
    s = input("请输入不带数字的文本:")
    p = 0
    for i in s:
        if "0"<=i<="9":
            p = p+1
    if p == 0:
        break
        
print(len(s))
