def findFirstOccurrence(nums, target):
    n = len(nums)
    left, right = 0, n - 1 
    result = -1 
    while left <= right:
        mid = (left + right) // 2 
        if nums[mid] == target:
            result = mid 
            left = mid + 1 
            if nums[left+1]!=target:
                c=0
                k=left
                while nums[k]!=target:
                    c+=1
                    k-=1
        elif nums[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1 
 
    return (result,c)
 
nums = [1, 2, 3, 4, 4, 4, 4, 6, 7]
print(findFirstOccurrence(nums, 4))
print(findFirstOccurrence(nums, 7))
print(findFirstOccurrence(nums, 41))