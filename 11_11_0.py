def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # xor
    # a number xor zero will be number where itself will be zero
    
    check_single = 0
    for num in nums:
        check_single ^= num
    return check_single

array = [4,1,2,1,2]

print(singleNumber(array))