## Question
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

---
## Notes
Challenges
- Words are not of the same length, so cannot just swap out
- If cycling, how to add spaces between words
    - Observation: A space will be present if they are indeed two different words
    - Observation: either give each word a leading space or a trailing space, and use that as marker when cycling

Naive solution
- Split by `' '`
- reverse using built in methods
- join by `' '`

Construction method
- start with two pointers from the end
- freeze first when the last letter of a word is reached
- freeze second when a space or start of string is reached
- copy over to new array and set first pointer to second pointer's location
- repeat until both pointers each start of string
- iterate array and join with a space

In-Place method
- Resize the string to include a space to the end of the string
- Set a pointer (A) from the left, indicating start of window
- Start a pointer (B) from the right, indicating end of window
- Move B towards the left, until a letter is met, and then expand window by one position to include marking spacer
- Cycle the string rightwards once, to move the marking spacer to the start of the string
- Cycle the string rightwards in the window, one letter at a time, until a space is at B again. This indicates one complete word has been cycled (along with a spacer)
- Move A towards the right, until a space is met, removing the newly cycled word outside of the window
- Repeat from step 4 until A meets or exceeds B
- Resize the string until B

In-Place Method (without an extra space!) - Community Method
- Reverse the whole string
- Set up a window and a pointer at start of string
- Move pointer to end ("start") of a reversed word
- Shift a word letter by letter, while expanding end of window to cover the whole word
- Reverse the letters in the window
- Add a space after reversed word (if no shift happened, this will replace the existing space)
- Reset window to the character after space, move index past the ("copied") space as well
- Repeat from step 3 until index is past string length
- Resize string until one character before the last window
