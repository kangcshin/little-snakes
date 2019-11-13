def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for i in range(len(nums)):
        if target - nums[i] in seen:
            return [i, seen[target-nums[i]]]
        else:
            seen[nums[i]] = i
    
    return 0

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))