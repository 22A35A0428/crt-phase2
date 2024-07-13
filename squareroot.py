def squareroot(n):
    left,right=1,n
    r=1
    while left<=right:
        mid=(left+right)//2
        if mid*mid<=n:
            left=mid+1
            r=mid
        else:
            right=mid-1
    return r

ans=squareroot(10)
print(ans)