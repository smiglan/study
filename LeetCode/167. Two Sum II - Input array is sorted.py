# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 04:06:16 2020

@author: migla
"""

# Approach 1: Two Pointers
# Algorithm

# We can apply Two Sum's solutions directly to get O(n^2)O(n 
# 2
#  ) time, O(1)O(1) space using brute force and O(n)O(n) time, O(n)O(n) space using hash table. However, both existing solutions do not make use of the property where the input array is sorted. We can do better.

# We use two indexes, initially pointing to the first and last element respectively. Compare the sum of these two elements with target. If the sum is equal to target, we found the exactly only solution. If it is less than target, we increase the smaller index by one. If it is greater than target, we decrease the larger index by one. Move the indexes and repeat the comparison until the solution is found.

# Let [... , a, b, c, ... , d, e, f, ...][...,a,b,c,...,d,e,f,...] be the input array that is sorted in ascending order and the element bb, ee be the exactly only solution. Because we are moving the smaller index from left to right, and the larger index from right to left, at some point one of the indexes must reach either one of bb or ee. Without loss of generality, suppose the smaller index reaches bb first. At this time, the sum of these two elements must be greater than target. Based on our algorithm, we will keep moving the larger index to its left until we reach the solution.
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_index = 0
        last_index = len(numbers)-1
        while(first_index < last_index):
            if numbers[first_index]+numbers[last_index] == target:
                return [first_index+1,last_index+1]
            elif numbers[first_index]+numbers[last_index] < target:
                first_index = first_index+1  
            elif numbers[first_index]+numbers[last_index] > target:
                last_index = last_index-1