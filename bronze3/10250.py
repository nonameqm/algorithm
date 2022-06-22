TEST_N=int(input())

room_str=''
floor_str=''
result=[]
for _i in range(TEST_N):
    h, w, n=map(int, input().split())
    room_number=n//h+1
    floor_number=n%h

    if(floor_number==0):
        floor_number=h
        room_number-=1

    print(floor_number*100+room_number)

