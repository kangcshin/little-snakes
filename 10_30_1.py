def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:k]
    

array = [1,2,3,4,5,6,7]
k = 3
print(array)
rotate(array, k)
print(array)