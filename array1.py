def removeDuplicates(nums):
    if not nums:
        return 0
    
    idx = 0
    
    for i in range(1,len(nums)):
        if nums[idx] != nums[i]:
            idx += 1
            nums[idx] = nums[i]

    return idx+1

array = [1,1,2]

out = removeDuplicates(array)
print(out)
