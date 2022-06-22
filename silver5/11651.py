import sys


N=int(sys.stdin.readline())


coords=[]
while(N>0):
    x, y=map(int, sys.stdin.readline().split())
    coords.append((x, y))
    N-=1

coords.sort(key=lambda x: (x[1], x[0]))

for coord in coords:
    print(coord[0], coord[1])