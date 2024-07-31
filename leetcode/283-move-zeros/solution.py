def moveZeros(nums):
    r_head, w_head = 0, 0
    while r_head < len(nums):
        while r_head < len(nums) and nums[r_head] != 0:
            nums[w_head] = nums[r_head]
            r_head += 1
            w_head += 1
        while r_head < len(nums) and nums[r_head] == 0:
            r_head += 1
    while w_head < len(nums):
        nums[w_head] = 0
        w_head += 1
    return None


nums = [1, 0, 2, 0, 3, 0]
moveZeros(nums)
expected = [1, 2, 3, 0, 0, 0]
assert nums == expected

nums = [-1, 0, 0, -2, 0, -3]
moveZeros(nums)
expected = [-1, -2, -3, 0, 0, 0]
assert nums == expected

nums = [0]
moveZeros(nums)
expected = [0]
assert nums == expected

