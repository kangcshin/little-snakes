def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    
    #.get(,)
    
    hashtable = {}
    output = []
    for num in nums1:
        hashtable[num] = hashtable.get(num,0) + 1
    for num in nums2:
        if hashtable.get(num) > 0:
            output.append(num)
            hashtable[num] -= 1
    return output


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1, nums2))