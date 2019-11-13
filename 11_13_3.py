def isAnagram(s, t):
    s_dict, t_dict = {}, {}
    
    for c in s:
        s_dict[c] = s_dict.get(c,0) + 1
    for c in t:
        t_dict[c] = t_dict.get(c,0) + 1
    return s_dict == t_dict
    
    
    
#         s_count = Counter(s)
#         t_count = Counter(t)
    
#         return s_count == t_count

s = "anagram"
t = "nagaram"

print(isAnagram(s, t))