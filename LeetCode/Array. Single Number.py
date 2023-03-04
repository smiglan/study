# # -*- coding: utf-8 -*-
# """
# Created on Mon Oct  5 07:16:13 2020

# @author: migla
# """
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

from collections import Counter
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Approach1 : List
        # no_duplicate_list = []
        # for i in nums:
        #     if i not in no_duplicate_list:
        #         no_duplicate_list.append(i)
        #     else:
        #         no_duplicate_list.remove(i)
        # return no_duplicate_list.pop()

        
        #Approach2 : Hash Table
        #         h = defaultdict(int)
#         for n in nums:
#             h[n] += 1
#         for i in h:
#             if h[i] == 1:
#                 return i
        
    
        #Approach3 : Math
        # return 2*sum(set(nums))-sum(nums)
#         Approach 4: Bit Manipulation
# Concept

# If we take XOR of zero and some bit, it will return that bit
# a \oplus 0 = aa⊕0=a
# If we take XOR of two same bits, it will return 0
# a \oplus a = 0a⊕a=0
# a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# So we can XOR all bits together to find the unique number.
        a = 0
        for i in nums:
            a ^= i
        return a
    
        #Approach 5: Counter
        # c = Counter(nums)
        # for n in set(nums):
        #     if c[n] == 1:
                # return n
#         h = {}
#         for n in nums:
#             if n not in h:
#                 h['one'] = n
#             elif n in h:
#                 h['two'] = n
#         return h['one']
                
            
            
            
        