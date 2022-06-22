import sys

def binary_search(start, end):
    if(start>end):
        return end

    mid=(start+end)//2
    ans=0
    for rope in ropes:
        ans+=(rope//mid)

    if ans>=n:
        return binary_search(mid+1, end)
    else:
        return binary_search(start, mid-1)




k, n=map(int, sys.stdin.readline().split())
i=0
ropes=[]
while(i<k):
    ropes.append(int(sys.stdin.readline()))
    i+=1

start=1
end=max(ropes)
print(binary_search(start, end))