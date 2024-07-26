## Question
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

---
## Notes
Approach 1
- GCD of strings will have the same length as the GCD of the lengths of the input strings
- If the every GCD length subdivision of both strings match up, then we have the GCD

Approach 2 (Community solution)
- If two strings are made of repeating atomic unit, then concatenating them will result in a longer string with the same atomic unit
- Concatenation will be commutative if both strings are made of the same repeating atomic unit
