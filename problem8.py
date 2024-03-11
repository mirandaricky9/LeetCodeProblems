# Problem #8
# Name: Ricardo Miranda
# Date: 3/11/24
# Completion Date: 3/11/24
# Description: Implement the *myAtoi(string s) function, which converts a string to a 32-bit
# signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. 
# Read this character in if it is either. 
# This determines if the final result is negative or positive respectively. 
# Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end 
# of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
# If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
# then clamp the integer so that it remains in the range. 
# Specifically, integers less than -231 should be clamped to -231, 
# and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.





class Solution:
     def myAtoi(self, s: str) -> int:

        s = s.strip() # removing white space
        isNeg = False
        num = ""

        if s == "":
            return 0

        # check to see if negative
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                isNeg = True
                s = s.replace("-","",1)
            elif s[0] == "+":
                s = s.replace("+","",1)

        # For loop going through the string
        for i in s:
            # checking to see if it is a number we are reading
            if i.isnumeric() == True:
                num += i
            else:
                break
        if num == "":
            num = "0"
        intNum = int(num)
        if isNeg:
            intNum = intNum * -1  
        
        # checking to see if 32 bit
        if (intNum < -2**31) or (intNum > 2**31 - 1):
            if isNeg:
                return -2**31
            else:
                return 2**31 -1
        else:
            return intNum


















# Test cases below: 

tester = Solution()

# print(tester.myAtoi("123"))
# print(tester.myAtoi("123 has words"))
# print(tester.myAtoi("-123"))
# print(tester.myAtoi("+123"))
print(tester.myAtoi("++1"))
# print(tester.myAtoi("+-12"))
# print(tester.myAtoi("-91283472332"))