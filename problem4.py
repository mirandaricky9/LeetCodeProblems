# Problem 4: Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n, respectively,
# return the median of the two sorted arrays. Time complexity should be
# O(log(m +n))

# Solution drafted by Ricardo Miranda 3/4/2024
# class Solution1:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         newArray = []
#         isTrue = True
#         if len(nums1) < len(nums2):
#             max = len(nums1)
#         else:
#             max = len(nums2)
#         pointerNums1 = 0
#         pointerNums2 = 0
#         while isTrue:
#             if (nums1[pointerNums1] < nums2[pointerNums2]):
#                 newArray.append(nums1[pointerNums1])
#                 pointerNums1 += 1
#             elif (nums2[pointerNums2] < nums1[pointerNums1]):
#                 newArray.append(nums2[pointerNums2])
#                 pointerNums2 += 1
#             elif (nums2[pointerNums2] == nums1[pointerNums1]):
#                 newArray.append(nums2)
#                 pointerNums1 += 1
#                 pointerNums2 += 1
#             break
#         return ""





# better solution might be to get the max size of the shortest array and then compare 
# until one of the arrays runs out


# Easier solution using sort from python

class Solution2:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        newArray = []
        # Have to iterate through the arrays, otherwise, you will append entire arrays into an array
        for i in nums1:
            newArray.append(i)
        
        for i in nums2:
            newArray.append(i)

        newArray.sort()
        print(newArray)
        # if the length of newArray is odd
        if len(newArray) % 2 == 1:
            median = newArray[len(newArray) // 2 ]
        else:  # even
            medianIndex = int((len(newArray) / 2) - 1) # division causes ints to become floats, so must type cast to int
            median = (newArray[medianIndex] + newArray[medianIndex + 1]) / 2
        
        return median

# Test cases: 
nums1 = [1,2]
nums2 = [3,4]

test2 = Solution2()
print(test2.findMedianSortedArrays(nums1, nums2))