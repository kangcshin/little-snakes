def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    converted_string = ''
    for c in s:
        if c.isalnum():
            converted_string += c
    converted_string = converted_string.lower()
    return converted_string == converted_string[::-1]


string = "A man, a plan, a canal: Panama"
# Output = True

print(isPalindrome(string))