def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    
    index = 0
    for i in range(1, len(nums)):
        if nums[index] != nums[i]:
            index += 1
            nums[index] = nums[i]
    print(nums)
    return index+1

nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))