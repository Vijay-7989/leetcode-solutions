"""
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.

Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters in word are 'a', 'b', and 'c'.

Example 2:
Input: word = "abc"
Output: 0
Explanation:
No character in word appears in uppercase.

Example 3:
Input: word = "abBCab"
Output: 1
Explanation:
The only special character in word is 'b'.

Constraints:
1 <= word.length <= 50
word consists of only lowercase and uppercase English letters.
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        check = set()
        word = set(word)
        special = 0
        for i in word:
            if i.islower() and i.upper() in check:
                special+=1
            elif i.isupper() and i.lower() in check:
                special+=1
            else:
                check.add(i)
        return special
                
