# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:00:04 2020

@author: migla
"""
# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
#         a = []
#         node1 = head

#         while node1:
#             a.append(node1.val)
#             node1 = node1.next
#         node1 = head
#         i = len(a)-1
#         while node1:
#             node1.val = a[i]
#             i = i-1
#             node1 = node1.next
            
#         head2 = ListNode()

#Recursive
    #      if (head == null || head.next == null) return head;
    # ListNode p = reverseList(head.next);
    # head.next.next = head;
    # head.next = null;
    # return p;
        
    
        node1 = head
        prev = node1

        # prev = node1
        # nextt = node1.next.next
        i = 0
        while node1:
            prev = node1
            node1 = node1.next
            if i == 0:
                # prev = temp
                prev.next = None
                temp = prev
                i += 1
                # print(prev)
            else:
                prev.next = temp
                temp = prev
            
        # print(prev)     
        return prev
    
#         def insert_node(node,value):
#             node.val = value
            
#             node.next = None
        
        
        