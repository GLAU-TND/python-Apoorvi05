n = int(input("enter the limit of bottles"))
res = list(map(int, input().split()))
print(max([res.count(i) for i in res]))
