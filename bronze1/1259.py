def palindrome(x):
    start=0
    end=len(x)
    for i in range(start, end//2, 1):
        if(x[i]!=x[end-1-i]):
            return False
    
    return True
            




array =[]
while(1):
    data=input()
    if(data=='0'):
        break
    array.append(data)

for item in array:
    if palindrome(item):
        print('yes')
    else:
        print('no')