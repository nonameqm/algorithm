import sys
from collections import deque, Counter

def avg(array):
    result=0
    for i in range(len(array)):
        result+=array[i]
    return round(result/len(array), 0)


N=int(sys.stdin.readline())
n=N
nums=deque()
while(n>0):
    num=int(sys.stdin.readline())
    nums.append(num)
    n-=1

cnt=Counter(nums).most_common()

print(int(avg(nums)))
sort_nums=sorted(nums)
print(sort_nums[N//2])
cnt=Counter(sort_nums).most_common()

if len(cnt)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(sort_nums[-1]-sort_nums[0])