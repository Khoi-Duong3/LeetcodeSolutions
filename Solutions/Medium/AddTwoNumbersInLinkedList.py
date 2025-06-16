# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumList = ListNode()
        carry = 0
        current = sumList

        while l1 or l2 or carry:

            if l1:
                value1 = l1.val
            else:
                value1 = 0
            
            if l2:
                value2 = l2.val
            else:
                value2 = 0
            
            sumVal = value1 + value2 + carry
            if sumVal >= 10:
                sumVal -= 10
                carry = 1
            else:
                carry = 0
            
            current.next = ListNode(sumVal)
            current = current.next
            
            if l1:
                l1 = l1.next
            else:
                None
            if l2:
                l2 = l2.next
            else:
                None
        
        return sumList.next
            





