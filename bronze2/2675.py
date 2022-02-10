n=int(input())

array=[]
for i in range(n):
    data=input().split()
    iter, string=data[0], data[1]
    array.append((iter, string))

for item in array:
    result=''
    char_list=list(item[1])
    for char in char_list:
        result+=char*int(item[0])
    print(result)
    