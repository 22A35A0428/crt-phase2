def binarysearch(nums,k,left,right):
    if left>right:
        return 'not found'
    mid=(left+right)//2
    if nums[mid]==k:
        return mid
    elif nums[mid]<k:
        return binarysearch(nums,k,mid+1,right)
    return binarysearch(nums,k,left,mid-1)
    
nums=[1,2,3,55,99,770,1000]
k=5
n=len(nums)
p=binarysearch(nums,k,0,n)
print(p)