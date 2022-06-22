a, b, v=map(int, input().split())


#General Solution
# ans=0
# while(v>0):
#     ans+=1
#     v-=a;
#     if(v<=0):
#         print(ans)
#         break
#     v+=b

ans=(v-a)//(a-b)
if (v-a)%(a-b)==0:
    print(int(ans+1))
else:
    print(int(ans+2))
