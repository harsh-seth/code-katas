from math import gcd

def gcdOfStrings(str1, str2):
    str1_len, str2_len = len(str1), len(str2) # O(1)
    gcdLen = gcd(str1_len, str2_len) # O(len(str2))
    gcdStr = str1[:gcdLen] # possible GCD

    for i in range(0, max(str1_len, str2_len), gcdLen): # O(len(str1))
        if i < str1_len and str1[i:i+gcdLen] != gcdStr:
            return ""
        if i < str2_len and str2[i:i+gcdLen] != gcdStr:
            return ""
    return gcdStr


str1 = "ABCABC"
str2 = "ABC"
assert gcdOfStrings(str1, str2) == "ABC"

str1 = "ABABAB"
str2 = "ABAB"
assert gcdOfStrings(str1, str2) == "AB"

str1 = "AAAAAAA"
str2 = "AAA"
assert gcdOfStrings(str1, str2) == "A"

str1 = "ABABCD"
str2 = "ABAB"
assert gcdOfStrings(str1, str2) == ""

str1 = "LEET"
str2 = "CODE"
assert gcdOfStrings(str1, str2) == ""
