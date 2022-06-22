import sys

L=int(sys.stdin.readline())

string=sys.stdin.readline()


result=0
i=0
for char in string[:-1]:
    result+=(ord(char)-96)*pow(31, i)
    i+=1
print(result%1234567891)