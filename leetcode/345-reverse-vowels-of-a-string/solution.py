def reverseVowels(s):
    i, j = 0, len(s)-1
    letters = list(s)
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    while i < j:
        if letters[i] in vowels and letters[j] in vowels:
            temp = letters[i]
            letters[i] = letters[j]
            letters[j] = temp
            i += 1
            j -= 1
        if letters[i] not in vowels:
            i += 1
        if letters[j] not in vowels:
            j -= 1

    return ''.join(letters)

str = "hello"
expected = "holle"
assert reverseVowels(str) == expected

str = "hEllO"
expected = "hOllE"
assert reverseVowels(str) == expected

str = "help"
expected = "help"
assert reverseVowels(str) == expected

str = "leetcode"
expected = "leotcede"
assert reverseVowels(str) == expected
