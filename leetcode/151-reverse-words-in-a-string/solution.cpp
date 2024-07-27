#include <string>
#include <cassert>
#include <iostream>
using std::string;

string reverseWords(string s) {
    int i = 0;
    int j = s.length();
    s.resize(j + 1, ' ');
    while (i <= j) {
        // Shrink window until the end of last word is met
        while (s[j] == ' ') j--;
        j++; // Expand window to incorporate a single space
        
        // Cycle string by 1 letter to the right to move space to start of string
        char temp = s[j];
        for(int k=j; k>i; k--) {
            s[k] = s[k-1];
        }
        s[i] = temp;

        // Cycle one word to the right
        while (s[j] != ' ') {
            // Cycle string by 1 letter to the right
            char temp = s[j];
            for(int k=j; k>i; k--) {
                s[k] = s[k-1];
            }
            s[i] = temp;
        }

        // Shrink window until the newly cycled word is outside of window
        while (s[i] != ' ') i++;
        i++; // Shrink window to exclude spacer for newly cycled word
    }
    s.resize(j);
    return s;
}

int main() {
    string s = "the sky is blue";
    string expected = "blue is sky the";
    assert(reverseWords(s) == expected);

    s = "  hello world  ";
    expected = "world hello";
    assert(reverseWords(s) == expected);

    s = "a good    example";
    expected = "example good a";
    assert(reverseWords(s) == expected);

    s = " alice ";
    expected = "alice";
    assert(reverseWords(s) == expected);
}
