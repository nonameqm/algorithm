data=list(map(int, input().split()))

number=0
for item in data:
    number+=item**2

print(number%10)