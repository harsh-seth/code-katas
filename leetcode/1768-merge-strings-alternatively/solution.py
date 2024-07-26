def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    i = 0
    word1_len, word2_len = len(word1), len(word2)
    # repeat until both string are exhausted
    while True:
        if i >= word1_len:
            # add remainder of word2 to result if word1 is exhausted
            result += word2[i:]
            break
        if i >= word2_len:
            # add remainder of word1 to result if word2 is exhausted
            result += word1[i:]
            break

        # add letters alternatively to result if both words aren't exhausted yet
        result += word1[i]
        result += word2[i]
        i += 1
    return result


str1 = "abc"
str2 = "pqr"
expected = "apbqcr"
assert mergeAlternately(str1, str2) == expected

str1 = "ab"
str2 = "pqrs"
expected = "apbqrs"
assert mergeAlternately(str1, str2) == expected

str1 = "abcd"
str2 = "pq"
expected = "apbqcd"
assert mergeAlternately(str1, str2) == expected

str1 = "abc"
str2 = ""
expected = "abc"
assert mergeAlternately(str1, str2) == expected

str1 = ""
str2 = "pqr"
expected = "pqr"
assert mergeAlternately(str1, str2) == expected
