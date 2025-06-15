# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        first = head
        left = head

        while first:
            length += 1
            first = first.next
        
        removeIndex = length - n
        if (removeIndex == 0):
            return head.next
        
        count = 0
        while count+1 < removeIndex:
            count += 1
            left = left.next
        
        left.next = left.next.next
    
        return head

        