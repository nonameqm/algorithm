import sys

N=int(sys.stdin.readline())

size=0
queue=[]

while(N>0):
    order=sys.stdin.readline().split()
    if order[0]=='push':
        queue.append(order[1])
        size+=1
    elif order[0]=='pop':
        if size==0:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
            size-=1
    elif order[0]=='size':
        print(size)
    elif order[0]=='empty':
        if size==0:
            print(1)
        else:
            print(0)
    elif order[0]=='front':
        if size==0:
            print(-1)
        else:
            print(queue[0])
    elif order[0]=='back':
        if size==0:
            print(-1)
        else:
            print(queue[len(queue)-1])
    else:
        print("Error")
    N-=1