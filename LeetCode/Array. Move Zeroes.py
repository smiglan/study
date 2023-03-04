# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 07:44:14 2020

@author: migla
"""


# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for n in nums:
        #     if n == 0:
        #         nums.remove(0)
        #         nums.append(0)
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                if explorer == anchor:
                    anchor+=1
                    continue
                else:
                    nums[anchor],nums[explorer] = nums[explorer],nums[anchor]
                    anchor += 1
            
      