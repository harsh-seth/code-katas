// https://leetcode.com/problems/reverse-words-in-a-string/solutions/4884894/best-explanation-with-photos-without-extra-space-beats-100-in-time-95-in-space
#include <string>
#include <algorithm>
#include <cassert>
using std::string;

string reverseWords(string s) {
    int n = s.size();
    int left = 0;
    int right = 0;
    int i = 0;

    std::reverse(s.begin(),s.end());
    while(i < n){
        while(i < n && s[i] == ' ') i++;
        if(i == n) break; // to stop index going out of bounds

        while(i < n && s[i] != ' ') {
            s[right++] = s[i++];
        }

        std::reverse(s.begin() + left, s.begin() + right);

        s[right++] = ' ';

        left = right;
        i++;
    }

    s.resize(right-1);
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
