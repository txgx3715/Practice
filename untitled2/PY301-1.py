# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open(r"C:\WEXAM\000000000000\命运.txt","r").read()
for i in "，。？：":
    f = f.replace(i,"")#通过对文本的遍历去除文章中的标点符号
d = {}
for x in f:
    d[x] = d.get(x,0)+1#统计出现在文章中的字符个数，出现一次加一
ls = list(d.items())#将统计在字典中的数据转化到列表中
ls.sort(key = lambda x:x[1],reverse = True)#由高到低逆向排序
a,b = ls[0]
print("{}:{}".format(a,b))
