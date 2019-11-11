def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    number = 0
    output = []
    for digit in digits:
        number = number*10 + int(digit)
    number += 1
    for num in str(number):
        output.append(num)
        
    return output

array = [4,3,2,1]

print(plusOne(array))