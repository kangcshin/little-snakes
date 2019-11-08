def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    

input_array = [1,2,3,4,5,6,7]
k = 3

print(input_array)
rotate(input_array, k)
print(input_array)