# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 04:32:48 2020

@author: migla
"""
from typing import List
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        output = -1
        #Solution 1 Brute force
#         for i,num in enumerate(A):
#             for j in range(i+1,len(A)):
#                 if A[i]+A[j]<K:
#                     if A[i]+A[j]>output:
#                         output = A[i]+A[j]
                    
#         return output 
        #Solution 2: Two pointers
        A = sorted(A)
        low = 0
        high = len(A)-1
        if len(A) > 1:
            if A[0]+A[1] > K:
                return -1
            while low < high:
                if A[low]+A[high] >= K:
                    high = high -1
                elif A[low]+A[high] < K:
                    output = max(A[low]+A[high],output)
                    low = low+1
            return output
        else:
            return -1
                

