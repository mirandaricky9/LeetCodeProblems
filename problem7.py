# Problem #7
# Name: Ricardo Miranda
# Date: 3/7/2024
# Completion Date: 3/7/2024
# Description: Given a signed 32-bit integer x, return x with its digits reversed. If reversing
# x causes the value to go outside the signed 32-bit integer range [-2^31 , 2^31 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        isNegative = (strX[0] == "-")
        strY = ""
        for i in range(len(strX) - 1, -1, -1):
            if (strX[i] != "-"):
                strY += strX[i]
        y = int(strY)
        if isNegative:
            y = -1 * y
            
        if y.bit_length() > 31:
            return 0

        return y















# Test cases below: 

tester = Solution()

# print(tester.reverse(-123))
# print(tester.reverse(1230))
print(tester.reverse(1463847412))
# print(tester.reverse(10023124798123921))

