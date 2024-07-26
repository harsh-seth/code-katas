from math import gcd

def gcdOfStrings(str1, str2):
    return str1[:gcd(len(str1), len(str2))] if (str1 + str2 == str2 + str1) else ""

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
