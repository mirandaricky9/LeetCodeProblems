# Problem #
# Name: Ricardo Miranda
# Date: 3/5/2024
# Description: Given a string s, return the longest palindromic substring in s.


# Pseudo code:

# while going through all possible substrings
    # check if substring is a palindrome
    # if not, move on
    # if it is, check to see if length of palindromic substring is longest than length of current palindrome
    # Base case for palindrome is empty string "" with length 0 


class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        print("The size of the string is {}.".format(size))
        longPalindrome = ""
        # starting point
        for i in range(0, size):
            print(i)
            # slider
            for j in range(i, size + 1): # dealing with two functions that have a "minus 1" tendency, range, and slice
                print(s[i:j]) # this will get all possibly substrings, now all that is left is to check each substring to see if it is a palindrome















# Test cases below: 

tester = Solution()
s = "abbd"
tester.longestPalindrome(s)

