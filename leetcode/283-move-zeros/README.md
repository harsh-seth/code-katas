## Question

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 

Constraints:
- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

---
## Notes

- This feels like it can be done with the sliding window/two pointer/shift left pattern
- Should we target 0s or non-0s?
    - Target non-zeros, and then fill out the rest of the array with zeros
- Should we swap elements, or shift everything?
    - Swap elements will work in tandem with the fill out method

Approach 1:
- Set `w_head` and `r_head` to the start of the array
- Move the `r_head` rightwards until a zero is met, copying over elements to the `w_head`
- Move the `r_head` over all the zeros until a non-zero is met
- Repeat from step 2 until the array is exhausted
- Fill out the rest of the array with zeros (from `w_head` till end of array)


Approach 2: (Pythonic)
- Pop and Append the 0, decreasing the total number of iterations with each zero
