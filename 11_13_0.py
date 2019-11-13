def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    for i in range(len(s)/2):
        s[i], s[-i-1] = s[-i-1], s[i]

input_s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"] INPLACE

print(input_s)
reverseString(input_s)
print(input_s)