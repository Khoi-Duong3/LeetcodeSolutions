# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findDuplicateNumber(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        while head:
            if head.val in seen:
                return head.val
            seen.add(head.val)
            head = head.next

        return -1