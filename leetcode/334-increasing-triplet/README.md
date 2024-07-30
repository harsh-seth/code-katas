## Question

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true

Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

- 1 <= nums.length <= 5 * 105
- -231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

---
## Notes

- The smallest 3 numbers should qualify?
- Track the max of the prefix, and if 3 different numbers come up, it is indeed true?
- Track the min of the suffix, and if 3 different numbers come up, it is indeed true?
- Do we need both tests or just one will suffice?
    - Need both tests, because of repeat numbers! [2, 0, 2, 4], [0, 2, 4, 2]
- Does not work! There can be an intermediary number: [5, 6, 2, 3, 1, 4]


Approach 1:
- Track the smallest number in the prefix
- Track the largest number in the suffix
- If a number is between the smallest (prefix) and the largest (suffix), then an increasing triplet exists

Approach 2: (Community)
- Track the smallest number in the prefix
- Track the smallest number that is larger than any of the previous smallest numbers in the prefix so far
- If a number is larger than both, then an increasing triplet exists
