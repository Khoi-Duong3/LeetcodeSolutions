"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None}

        temp = head
        
        while temp:
            copy = Node(temp.val)
            hashmap[temp] = copy
            temp = temp.next
        
        current = head
        while current:
            copy = hashmap[current]
            copy.next = hashmap[current.next]
            copy.random = hashmap[current.random]
            current = current.next
        
        return hashmap[head]