def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    out = ''
    for digit in digits:
        out += str(digit)
    out = int(out) + 1
    print([x for x in str(out)]) 

array = [4,3,2,1]

plusOne(array)