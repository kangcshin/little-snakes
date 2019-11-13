def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    keep = {}
    seen = set()

    for idx, c in enumerate(s):

        if c not in seen:
            keep[c] = idx
            seen.add(c)
        elif c in keep:
            del keep[c]
    return min(keep.values()) if keep else -1

    
input_string = "loveleetcode"
# return 2.

print(firstUniqChar(input_string))