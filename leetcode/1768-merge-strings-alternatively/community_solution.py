# Adapted from https://leetcode.com/problems/merge-strings-alternately/solutions/3429116/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/comments/1867241
def mergeAlternately(word1: str, word2: str) -> str:
    string = ""
    count = 0
    limit = min(len(word1), len(word2))
    while count < limit:
        string += word1[count]
        string += word2[count]
        
        count += 1
    return string + word1[count:] + word2[count:]


str1 = "abc"
str2 = "pqr"
expected = "apbqcr"
assert mergeAlternately(str1, str2), expected

str1 = "ab"
str2 = "pqrs"
expected = "apbqrs"
assert mergeAlternately(str1, str2), expected

str1 = "abcd"
str2 = "pq"
expected = "apbqcd"
assert mergeAlternately(str1, str2), expected

str1 = "abc"
str2 = ""
expected = "abc"
assert mergeAlternately(str1, str2), expected

str1 = ""
str2 = "pqr"
expected = "pqr"
assert mergeAlternately(str1, str2), expected

