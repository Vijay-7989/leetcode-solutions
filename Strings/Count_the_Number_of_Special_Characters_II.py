"""
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.

 

Constraints:

1 <= word.length <= 2 * 105
word consists of only lowercase and uppercase English letters.
"""


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        position = {}
        c = set()
        spec = 0
        for i in range(len(word)):
            if word[i].islower():
                position[word[i]] = i
            elif word[i].isupper() and word[i] not in position:
                position[word[i]] = i
        
        for i in word:
            if i.islower() and i.upper() in position:
                c.add(i)
        
        for i in c:
            if position[i] < position[i.upper()]:
                spec+=1
        
        return spec
