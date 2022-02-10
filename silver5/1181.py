n=int(input())
word_list=[]

for i in range(n):
    word=input()
    length=len(word)
    word_list.append((length, word))

word_list=list(set(word_list))
word_list.sort(key=lambda x: (x[0], x[1]))

for item in word_list:
    print(item[1])