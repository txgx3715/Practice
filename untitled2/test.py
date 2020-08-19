N = eval(input("请输入一个整数 :"))
sum = 0
for N in range(N,N+100):
    if N % 2 != 0:
        sum = N + sum

print(sum)
