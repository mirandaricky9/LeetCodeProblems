# Problem #9 - Palindrome Number
# Name: Ricky
# Date: March 19, 2024
# Completion Date: March 19, 2024
# Description: Given an integer x, return true if x is a palindrome, return false otherwise

# Examples
# 121 - outputs true
# -121 - outputs false
# 10 - outputs false


# Challenge: Could you solve it without converting the integer to a string?

# Constraints: -2**31 <= x <= 2**31 - 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # converting to a string method

        # strX goes left to right
        strX = str(x)

        strXReversed = strX[::-1]
        

        if (strX == strXReversed) and ((x <= 2**31 -1) and (x >= -2**31)):
            return True
        
        return False








# Test cases below: 

tester = Solution()

print(tester.isPalindrome(121))
print(tester.isPalindrome(-121))
print(tester.isPalindrome(10))
print(tester.isPalindrome(232))
print(tester.isPalindrome(1001))



