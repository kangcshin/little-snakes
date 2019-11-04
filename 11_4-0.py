def isIsomorphic(s, t):
    hashmap = {}
    seen = set()
    
    for i, j in zip(s, t):
        if i in hashmap:
            if j != hashmap[i]:
                print(False)
        else:
            if j in seen:
                print(False)
            seen.add(j)
            hashmap[i] = j
        
        print(True)

s = "egg"
t = "add"

isIsomorphic(s, t)