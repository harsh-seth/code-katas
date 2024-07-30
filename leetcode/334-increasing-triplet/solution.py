def increasingTriplet(nums):
    if len(nums) < 3:
        return False

    num_elems = len(nums)
    prefix = [nums[0]] * num_elems
    for i in range(1, num_elems):
        if nums[i] < prefix[i-1]: prefix[i] = nums[i]
        else: prefix[i] = prefix[i-1]
    
    suffix = [nums[-1]] * num_elems
    for i in range(num_elems-2, -1, -1):
        if nums[i] > suffix[i+1]: suffix[i] = nums[i]
        else: suffix[i] = suffix[i+1]
    
    for i in range(0, num_elems):
        if prefix[i] < nums[i] < suffix[i]: return True

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
