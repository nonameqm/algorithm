n=int(input())

user=[]
for _ in range(n):
    a, b = map(int, input().split())
    user.append((a, b))
    
result=[]
for i in range(n):
    d=1
    for j in range(n):
        if i==j:
            continue
        else:
            if user[i][0]<user[j][0] and user[i][1]<user[j][1]:
                d+=1
    result.append(d)

for item in result:
    print(item, end=" ")