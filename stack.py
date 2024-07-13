def hi(k,ele):
    s.append(ele)
    

def yes(s):
    if len(s)==0:
        print('emt')
        return
    print(s[-1])
    k.append(s[-1])
    s.pop()

s=[]
k=[]
hi(s,104)
hi(s,19)
hi(s,18)#s is varible
hi(s,15)
hi(s,10)
print(s)

# yes(s)
# yes(s)


for i in range(len(s)):
    yes(s)
print(k)