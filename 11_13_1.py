def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    sign = 1
    output = ''
    
    if x < 0:
        sign = -1
        x = abs(x)

    string_input = str(x)

    for i in reversed(range(len(string_input))):
        output += string_input[i]
    return int(output) * sign

input_number = 120
# output = 21

print(reverse(input_number))