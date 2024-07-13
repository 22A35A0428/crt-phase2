n,m=map(int,input().split())
mat=[]
for i in range(n):
    row=[0]*n
    mat.append(row)

print(mat)
for i in range(m):
    u,v=map(int,input().split())
    mat[u][v]=1
    mat[v][u]=1
print(mat)
