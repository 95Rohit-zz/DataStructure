# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        output = []
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            find = (-1)* nums[i]
            while j < k:
                if nums[j] + nums[k] == find:
                    temp = [nums[i],nums[j],nums[k]]
                    temp = sorted(temp)
                    if temp not in output:
                        output.append(temp)
                    k = k-1
                    j = j+1
                elif nums[j] + nums[k] > find:
                    k = k-1
                else:
                    j = j+1
        return output
