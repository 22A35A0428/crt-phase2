def hi(ele):
    q.append(ele)
    print(ele)
    
def deq(q):
    if len(q)==0:
        print('sorry')
        return
    print(q[0])
    k.append(q[0])
    q.pop(0)


q=[]
k=[]
n=[10,11,21,22,29,35]
for num in n:
    hi(num)

for i in range(len(n)+1):
    deq(q)
print(k)
