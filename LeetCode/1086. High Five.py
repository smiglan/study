# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 05:46:03 2020

@author: migla
"""
from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = {}
        for i,v in items:
            if i not in scores:
                scores[i] = [v]
            else:
                scores[i].append(v)
        output = []
        for key,value in scores.items():
            output.append([key,sum(sorted(value)[-5:])//5])
        return output
#         D = collections.defaultdict(list)
#         for student,score in items:
#             bisect.insort(D[student],score)
#         return [[student,sum(D[student][-5:])//5] for student in D]
    
       