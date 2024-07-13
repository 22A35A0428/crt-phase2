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


# Adjacency Matrix
# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     row = [0] * n 
#     # [0, 0, 0, 0, 0]
#     matrix.append(row)
 
# print(matrix)  
# for i in range(m):
#     u, v = map(int, input().split())
#     matrix[u][v] = 1 
#     matrix[v][u] = 1  
 
# print(matrix)
 
 


# n,m=map(int,input().split())
# a=[]
# for i in range(n):
#     r=[0]*n
#     a.append(r)

# for i in range(m):
#     u,v=map(int,input().split())
#     a[u][v]=1
#     a[v][u]=1
# print(a)