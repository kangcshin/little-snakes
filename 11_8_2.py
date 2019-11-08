def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    unique = set(nums)
    return len(unique) != len(nums)
    
    
    
array = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate(array))
    