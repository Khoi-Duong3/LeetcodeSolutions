# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
            
        for i in range (1, len(lists)):
            mergedList = self.mergeTwoLinkedLists(lists[i-1], lists[i])
            lists[i] = mergedList
        
        return lists[-1]
    
    def mergeTwoLinkedLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    current.next = ListNode(l1.val)
                    current = current.next
                    l1 = l1.next
                elif l2.val < l1.val:
                    current.next = ListNode(l2.val)
                    current = current.next
                    l2 = l2.next
                else:
                    current.next = ListNode(l1.val)
                    current = current.next
                    current.next = ListNode(l2.val)
                    current = current.next
                    l1 = l1.next
                    l2 = l2.next
            
            if l1:
                current.next = l1

            if l2:
                current.next = l2
            
            return dummy.next
            
