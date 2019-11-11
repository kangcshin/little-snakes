def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    pointer = 0
    
    for num in nums:
        if num != 0:
            nums[pointer] = num
            pointer += 1
    while pointer < len(nums):
        nums[pointer] = 0
        pointer += 1

array = [0,1,0,3,0,0,5,0,7,12]

print(array)
moveZeroes(array)
print(array)