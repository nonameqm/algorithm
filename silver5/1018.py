n, m=map(int, input().split())
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

data=[]
result_array=[]

def compare_model(data, model):
    count=0
    for i in range(8):
        for j in range(8):
            if (data[i][j]!=model[i][j]):
                count+=1
    return count

def get_datamodel(i, j):
    temp=[]
    for i in range(i, i+8):
        temp.append(data[i][j:j+8])
    return temp

for _ in range(n):
    data.append(input())
for i in range(0, n-7):
    for j in range(0, m-7):
        temp=get_datamodel(i, j)
        result_array.append(min(compare_model(temp, model1), compare_model(temp, model2)))
print(min(result_array))
