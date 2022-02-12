N=int(input())

data=[]
for _ in range(N):
    data.append(int(input()))

data.sort()

for item in data:
    print(item)