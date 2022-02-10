input=list(map(int, input().split()))
ascend_list=[1, 2, 3, 4, 5, 6, 7, 8]
descend_list=[8, 7, 6, 5, 4, 3, 2, 1]

if input==ascend_list:
    print('ascending')
elif input==descend_list:
    print('descending')
else:
    print('mixed')