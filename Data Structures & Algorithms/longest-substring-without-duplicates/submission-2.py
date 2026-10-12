'''
Understand
Inpput: A string with a letter put together
Output: a number of the amout of letter that where in order
Egde cases: What if we get empy, only one letter, or many of the same letter, how baout if it repeating characters, what if there is spaces

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)
        return res







        