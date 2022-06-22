N=int(input())
arr=list(map(int, input().split()))




def prime_number(x):
    if x==1:
        return False
    if x==2 or x==3:
        return True
    else:
        for i in range(2, x//2+1):
            if(x%i==0):
                return False
        return True

result=0
for item in arr:
    if prime_number(item)==True:
        result+=1

print(result)

