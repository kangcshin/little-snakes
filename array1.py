def removeDuplicates(nums):
    if not nums:
        return 0
    
    idx = 0
    
    for i in range(1,len(nums)):
        if nums[idx] != nums[i]:
            idx += 1
            nums[idx] = nums[i]
            
    print(idx+1)

removeDuplicates([1,1,2])