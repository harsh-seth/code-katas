def isSubsequence(s, t):
    if len(s) == 0:
        return True

    s_head = 0
    for t_head in range (0, len(t)):
        if t[t_head] == s[s_head]:
            s_head += 1
        if s_head == len(s):
            return True
        
    return False


s = 'ace'
t = 'abcde'
assert isSubsequence(s, t) == True

s = ''
t = 'abcde'
assert isSubsequence(s, t) == True

s = 'ace'
t = 'abcd'
assert isSubsequence(s, t) == False

s = 'ace'
t = ''
assert isSubsequence(s, t) == False

s = 'aed'
t = 'abcde'
assert isSubsequence(s, t) == False
