import sys
from collections import deque


def solution(sentence):
    i=0
    while(sentence[i]!='.'):
        if(sentence[i]=='('):
            stack.append(sentence[i])       
        elif(sentence[i]=='['):
            stack.append(sentence[i])
        elif(sentence[i]==')'):
            if len(stack)==0:
                return False
            else:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
        elif(sentence[i]==']'):
            if len(stack)==0:
                return False
            else:
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False      
        else:
            pass
        i+=1
    if len(stack)==0:
        return True
    else:
        return False

while(1):
    sentence=sys.stdin.readline()
    if(sentence[0]=='.'):
        break
    stack=deque()
    if solution(sentence)==True:
        print('yes')
    else:
        print('no')
        

