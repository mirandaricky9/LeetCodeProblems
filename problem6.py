# Problem #6
# Name: Ricky
# Date: 3/7/2024
# Completion Date: 3/7/2024
# Description: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
# Write the code that will take a string and make this conversion given a number of rows.



# messy and can be consolidated because the same code is being used in two different spots 

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # iterate over the entire string in one for loop and the number of rows will be the second and third for loops
        matrix = []
        finalString = ""
        strS = s # creating a copy to modify
        # set up the matrix
        for i in range(0, numRows):
            matrix.append([])
        # print(matrix) 
        # print(s[-1])
        while True:
            for j in range(0, numRows):
                    matrix[j].append(strS[0])
                    if strS == s[-1]:
                        for i in matrix:
                            for j in i:
                                finalString += j + ""
                        return finalString
                    strS = strS[1:]
                    # for i in matrix:
                    #     print(i)
                    # print(strS)

            # traversing the rows upwards and diagonal
            for j in range(numRows - 2, 0, -1):
                    matrix[j].append(strS[0])
                    if strS == s[-1]:
                        for i in matrix:
                            for j in i:
                                finalString += j + ""
                        return finalString
                    strS = strS[1:]
                    # for i in matrix:
                        # print(i)
                    # print(strS)

       

        
            

















# Test cases below: 

tester = Solution()

print(tester.convert("PAYPALISHIRING",3))


