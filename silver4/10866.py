import sys

N=int(sys.stdin.readline())

size=0
deck=[]

while N>0:
    order=sys.stdin.readline().split()

    if order[0]=='push_front':
        deck.insert(0, int(order[1]))
        size+=1
    elif order[0]=='push_back':
        deck.append(int(order[1]))
        size+=1
    elif order[0]=='pop_front':
        if size==0:
            print(-1)
        else:
            print(deck[0])
            deck.pop(0)
            size-=1
    elif order[0]=='pop_back':
        if size==0:
            print(-1)
        else:
            print(deck[len(deck)-1])
            deck.pop(len(deck)-1)
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
            print(deck[0])
    elif order[0]=='back':
        if size==0:
            print(-1)
        else:
            print(deck[-1])
    else:
        print('Error')
    N-=1
