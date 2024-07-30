import math


def increasingTriplet(nums):
    a, b = math.inf, math.inf # a = smallest number, b = small number larger than the smallest number
    for num in nums:
        if num <= a:
            a = num
        elif num <= b:
            b = num
        else:
            return True
    return False

nums = [1, 2, 3, 4, 5]
expected = True
assert increasingTriplet(nums) == expected

nums = [5, 4, 3, 2, 1]
expected = False
assert increasingTriplet(nums) == expected

nums = [2, 1, 5, 0, 4, 6]
expected = True
assert increasingTriplet(nums) == expected

nums = [2, 0, 2, 4]
expected = True
assert increasingTriplet(nums) == expected

nums = [0, 2, 4, 2]
expected = True
assert increasingTriplet(nums) == expected

nums = [5, 6, 2, 3, 1, 4]
expected = True
assert increasingTriplet(nums) == expected

nums = [5, 6, 2, 7]
expected = True
assert increasingTriplet(nums) == expected

