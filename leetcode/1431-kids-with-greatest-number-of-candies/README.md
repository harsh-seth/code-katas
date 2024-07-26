## Question

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50

---
## Notes
- Someone will always have the greatest number of candies
- It is not necessary that there will be someone who does not have the greatest number of candies
- Effectively, normalize the candies and add the offset, any one reaching a non-negative number will have the greatest after the extra candies
