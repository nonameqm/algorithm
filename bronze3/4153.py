result=[]
while(1):
    array=list(map(int, input().split()))
    if array==[0, 0, 0]:
        break
    d=max(array)
    array.remove(d)
    a, b=array[0], array[1]
    if int(a**2)+int(b**2)==int(d**2):
        result.append('right')
    else:
        result.append('wrong')

for item in result:
    print(item)
