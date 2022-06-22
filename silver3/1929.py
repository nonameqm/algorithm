def prime_number(x):
    if x==1:
        return False
    if x==2 or x==3:
        return True
    else:
        for i in range(2, int(x**0.5)+1):
            if(x%i==0):
                return False
        return True


m, n=map(int, input().split())


for i in range(m, n+1, 1):
    if prime_number(i):
        print(i)