from operator import index


n=int(input())

member_list=[]
for i in range(n):
    data=input().split()
    member_list.append([int(data[0]), data[1]])

member_list.sort(key=lambda x: (x[0], index))

for member in member_list:
    print(member[0], member[1])