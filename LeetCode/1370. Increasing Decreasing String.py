# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 04:58:32 2020

@author: migla
"""


class Solution:
    def sortString(self, s: str) -> str:
        result = ""

        while(len(s)>0):
            s1 = sorted(list(set(s)))
            for i in s1:
                result = result+i
                s = s.replace(i,"",1)
            if s:
                s1 = sorted(list(set(s))) 
                for i in range(len(s1)-1,-1,-1):
                    result = result+s1[i]
                    s = s.replace(s1[i],"",1)

        return result
        
        