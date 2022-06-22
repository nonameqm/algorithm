import sys

N=int(sys.stdin.readline())

size=0
stack=[]

while(N>0):
    order=sys.stdin.readline().split()
    if order[0]=='push':
        stack.append(int(order[1]))
        size+=1
    elif order[0]=='pop':
        if size==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
            stack.pop()
            size-=1
    elif order[0]=='size':
        print(size)
    elif order[0]=='empty':
        if(size==0):
            print(1)
        else:
            print(0)
    elif order[0]=='top':
        if size==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    else:
        print('Error')
    N-=1