def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    out = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            nums2.remove(nums1[i])
            out.append(nums1[i])
    print(out)

array1 = [1,2,2,1]
array2 = [2,2]

intersect(array1, array2)