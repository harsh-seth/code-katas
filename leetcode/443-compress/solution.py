def compress(chars): # modify chars in-memory and return new length of chars
    r_head, w_head = 0, 0
    while r_head < len(chars):
        counter, current_char = 0, chars[r_head]
        while r_head < len(chars) and chars[r_head] == current_char:
            counter += 1
            r_head += 1

        chars[w_head] = current_char
        w_head += 1
        if counter > 1:
            for char in list(str(counter)):
                chars[w_head] = char
                w_head += 1
    return w_head

chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
expected_chars = ['a', '2', 'b', '2', 'c', '3']
assert chars[:compress(chars)] == expected_chars

chars = ['a']
expected_chars = ['a']
expected_length = 1
assert chars[:compress(chars)] == expected_chars

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
expected_chars = ['a', 'b', '1', '2']
expected_length = 4
assert chars[:compress(chars)] == expected_chars
