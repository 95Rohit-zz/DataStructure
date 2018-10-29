# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#              or index number 5 where the peak element is 6.
# Note:

# Your solution should be in logarithmic complexity.



#SOLUTION 1 :- O(N)

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i
        return nums.index(max(nums))
        


#SOLUTION 2: O(NLogN)

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0
        return helper(nums,0,len(nums)-1)

def helper(nums,start,end):
    if start >= end:
        return start
    if end-start == 1:
        return nums.index(max(nums[start],nums[end]))
    mid = int((start+end)/2)
    if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
        return mid
    elif nums[mid-1] > nums[mid]:
        return helper(nums,start,mid-1)
    else:
        return helper(nums,mid+1,end)