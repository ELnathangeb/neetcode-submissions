'''
Understand
Inpput: A string with a letter put together
Output: a number of the amout of letter that where in order
Egde cases: What if we get empy, only one letter, or many of the same letter, how baout if it repeating characters, what if there is spaces

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Map = {}
        current_count = 0
        biggest = 0
        left = 0

        for right in range(len(s)):

            if s[right] in Map:
                left = max(left, Map[s[right]] + 1)

            Map[s[right]] = right

            current_count = right - left + 1

            if current_count > biggest:
                biggest = current_count

        return biggest
        






        