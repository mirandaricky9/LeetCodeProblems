# Problem #10 - Regular Expression Matching 
# Name: Ricky
# Date: March 19, 2024
# Completion Date: 
# Description: Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
    # '.' Matches any single character
    # '*' Matches zero or more of the preceding element

# Example 1:
#   Input: s = "aa", p = "a"
#   Output: false
#   Explanation: "a" does not match the entire string "aa".

# Example 2
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Constraints
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

# Example 4: 

# s = "aaaaa" p = "aaaaa" - outputs true 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # -------------------------------------
        # if the two strings are the same
        if (s == p):
            return True

        # potential routes to go, split the string at asterisk or dots, and try matching or generating
        # strings from there
        # listStr = []
        # genStr = ""
        # asterisk = False
        # if p.find("*"):
        #     while len(genStr) < 21:
        # -------------------------------------
        # for each char in p, grab both index and char
        sIndex = 0
        for index,char in enumerate(p):
            
            # check to see if character doesn't match same position in string
            if sIndex < len(s):
                if (char != s[sIndex]):
                    # check to see if it is '.' (any character)
                    if (char != '.'):
                        # check to see if it is a wildcard '*'abs
                        if (char != '*'):
                            return False
                        else:
                            prevChar = p[index - 1]
                            # if the previous character doesn't match the current index of the string, return false
                            if (prevChar != s[sIndex]):
                                return False
                            # if previous character in pattern does match
                            else:
                                while (prevChar == s[sIndex]) and (sIndex < len(s) - 1):
                                    sIndex = sIndex + 1
                                # might not be good practice 
                                sIndex = sIndex - 1
            sIndex = sIndex + 1
        print(sIndex)
        if (sIndex + 1) == len(s):
            return True

                

        return False






# Test cases below: 

tester = Solution()

# print(tester.isMatch("aaaaaaaaaaaaa","a*"))
# print(tester.isMatch("aaaa","a*"))
# print(tester.isMatch("aaaaaaaaaa","a*"))
# print(tester.isMatch("a","a*"))
print(tester.isMatch("acbbb","acb*"))

