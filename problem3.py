# Problem 3: Longest substring without repeating characters 
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # creating a set so there are no duplicates
        l = 0           # left hand pointer
        res = 0         # the result 
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
                

                


