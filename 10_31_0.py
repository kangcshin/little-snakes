import collections
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    counter = collections.Counter(nums)
    for num in nums:
        if counter[num] != 1:
            print(True)
    print(False)

array = [1,2,3,1]

containsDuplicate(array)