def kidsWithCandies(candies, extraCandies):
    # subtract the max from all the candies, to "normalize" the scale
    # add the extraCandies to see if any can beat the threshold
    # any one reaching a non-negative number will have the greatest after the extra candies

    offset = extraCandies - max(candies) # O(n)
    result = [(candy + offset)>=0 for candy in candies] # O(n)
    return result


candies = [2, 3, 5, 1, 3]
extraCandies = 3
assert kidsWithCandies(candies, extraCandies) == [True, True, True, False, True]

candies = [4, 2, 1, 1, 2]
extraCandies = 1
assert kidsWithCandies(candies, extraCandies) == [True, False, False, False, False]

candies = [12, 1, 12]
extraCandies = 10
assert kidsWithCandies(candies, extraCandies) == [True, False, True]
