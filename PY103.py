#
# 在____________上补充代码
#


std = [['张三',90,87,95],['李四',83,80,87],['王五',73,57,55]]
modl = "亲爱的{}, 你的考试成绩是: 英语{}, 数学{}, Python语言{}, 总成绩{}.特此通知."

for st in std:
    cnt = 0
    for i in range(1,4):
        cnt += st[i]
    print(modl.format(st[0],st[1],st[2],st[3],cnt))


