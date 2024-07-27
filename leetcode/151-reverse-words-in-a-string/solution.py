def reverseWords(s):
    words = s.split(' ')
    words = [word for word in words if word != '']
    words.reverse()
    return ' '.join(words)

s = "the sky is blue"
expected = "blue is sky the"
assert reverseWords(s) == expected

s = "  hello world  "
expected = "world hello"
assert reverseWords(s) == expected

s = "a good    example"
expected = "example good a"
assert reverseWords(s) == expected

s = " alice "
expected = "alice"
assert reverseWords(s) == expected
