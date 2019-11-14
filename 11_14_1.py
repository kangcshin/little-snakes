def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    
    needle_size = len(needle)
    
    for i in range(len(haystack) - needle_size + 1):
        if haystack[i:i+needle_size] == needle:
            return i
        
    return -1

haystack = "hello"
needle = "ll"
# Output 2

print(strStr(haystack, needle))