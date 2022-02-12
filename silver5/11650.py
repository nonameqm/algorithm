n=int(input())

data=[]

for _ in range(n):
    x, y=map(int, input().split())
    data.append((x, y))

data.sort(key=lambda x: (x[0], x[1]))

for item in data:
    print(item[0], item[1])