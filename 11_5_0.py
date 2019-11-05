def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    absent_counter = 0

    for i in range(len(s)):
        if s[i] == 'A':
            absent_counter += 1
            if absent_counter == 2:
                return False
        elif i < len(s) and s[i:i+3] == 'LLL':
            return False
    return True

record = "PPALLL"
record1 = "PPALLP"
print(checkRecord(record))
print(checkRecord(record1))