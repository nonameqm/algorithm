n, m=map(int, input().split())

data=[]
model1=[
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
model2=[
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]



for _ in range(n):
    data.append(input())

for i in range(0, n-7):
    for j in range(0, m-7):
        temp=data[i:i+8][j:j+8]

test=[0,1,2,3,4,5,6,7]
print(test[0:2])