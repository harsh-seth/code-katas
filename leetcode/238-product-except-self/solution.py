# requirements: (1) O(n) time (2) no division operator
def productExceptSelf(nums):
    num_elems = len(nums)
    answer = [1] * num_elems

    curr = 1
    for i in range(0, num_elems):
        answer[i] = curr
        curr *= nums[i]

    curr = 1
    for i in range(num_elems-1, -1, -1):
        answer[i] *= curr
        curr *= nums[i]
    return answer

nums = [1, 2, 3, 4]
expected = [24, 12, 8, 6]
assert productExceptSelf(nums) == expected

nums = [-1, 1, 0, -3, 3]
expected = [0, 0, 9, 0, 0]
assert productExceptSelf(nums) == expected

nums = [1, -1]
expected = [-1, 1]
assert productExceptSelf(nums) == expected
