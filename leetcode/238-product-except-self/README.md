## Question

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

---
## Notes
- The solution needs to be done in O(n) time and cannot use the division operation
- Division can be seen as
    - repeated subtraction (likely not allowed in this case)
    - multiplication of the inverse (likely not allowed in this case)
- Product can be seen as 
    - repeated addition (will break the O(n) case)
- Division will in any case fail, since some numbers can be 0s

Approach 1 (running train of multiplication)
- Initialize result to all 1s
- Rotate all of nums right-wards by 1 position
- Multiply every corresponding element
- Repeat n-1 times
REJECTED - Runtime: O(N^2 -N)

Approach 2 (prefix and suffix arrays)
- The product of all the left elements (prefix) * product of all the right elements (suffix) will yield the required result
- Accumulate the prefix multiplications, and the suffix multiplications
- Exclude the current number from the both the prefix and suffix to ensure that we meet the criteria
