n, m, b=map(int,input().split())

m_array=[]
m_dict={}
for _ in range(n):
    row=list(map(int, input().split()))
    for item in row:
        m_array.append(item)
        if item in m_dict.keys():
            m_dict[item]+=1
        else:
            m_dict[item]=1

print(m_dict)