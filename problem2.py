# Problem 2: Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy             # pointer at the start of the linked-list
        
        carry = 0
        while l1 or l2 or carry:         # while either list is not null
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            
            # new digit 
            val = v1 + v2 + carry
            # 15 as example
            carry = val // 10   # floor division
            val = val % 10 
            cur.next = ListNode(val) # create a new node 
            
            # update ptrs 
            cur = cur.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            
        return dummy.next