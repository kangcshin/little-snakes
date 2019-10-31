def singleNumber(nums):
    out = 0
    for num in nums:
        out ^= num
    print(out)

array = [4,1,2,1,2]
singleNumber(array)