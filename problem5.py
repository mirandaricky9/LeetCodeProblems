# Problem #
# Name: Ricardo Miranda
# Date: 3/5/2024
# Completion Date: 3/7/2024
# Description: Given a string s, return the longest palindromic substring in s.


# Pseudo code:

# while going through all possible substrings
    # check if substring is a palindrome
    # if not, move on
    # if it is, check to see if length of palindromic substring is longest than length of current palindrome
    # Base case for palindrome is empty string "" with length 0 


# Notes after completion: This is NOT the fastest way to do this but in my opinion, the simplest.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        # print("The size of the string is {}.".format(size))
        longPalindrome = ""
        # starting point
        for i in range(0, size):
            # slider
            for j in range(i, size + 1): # dealing with two functions that have a "minus 1" tendency, range, and slice
                #print(s[i:j]) # this will get all possible substrings, now all that is left is to check each substring to see if it is a palindrome
                substringF = s[i:j]
                substringB = substringF[::-1]
                if (substringB == substringF):
                    if (len(substringF) > len(longPalindrome)):
                        longPalindrome = substringF
                # print("The substring going forward is " + substringF)
                # print("The substring going backward is " + substringB)
        return longPalindrome















# Test cases below: 

tester = Solution()
s = "abbd"
print(tester.longestPalindrome(s))

