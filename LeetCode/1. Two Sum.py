# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 03:51:03 2020

@author: migla
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Solution 1: Time complexity O(n*n), Spacy complexity O(1)
#         for index,first in enumerate(nums):
#             for second in range(index+1,len(nums)):
#                 if first + nums[second] == target:
#                     print(first , nums[second])
#                     output = [index, second]
#                     return output
#                 else:
#                     continue
       # Solution 2: Time complexity O(n), Space complexity O(n)
       #Follow these steps
        # 1) Check if the difference of target - current number is in the hash map
        # 2) If it is not, add it to the hash map with the number as key and the index as value
        # 3) if it is return current index and the index from the hash map
        h = {}
        for i,num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n],i]
                    