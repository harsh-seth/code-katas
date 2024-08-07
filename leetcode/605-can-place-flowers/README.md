## Question
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

- 1 <= flowerbed.length <= 2 * 104
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length

---
## Notes
- A flowerbed can at max have ceil(n/2) flowers
- Patterns of empty spots can be: (0, 0, 0); ([0, 0); (0, 0])
    - appending 0 and 0 on both ends can make it a search for (0,0,0) patterns

