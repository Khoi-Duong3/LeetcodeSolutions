# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        result = []

        queue.append(root)

        while queue:
            layer = []
            for i in range(len(queue)):
                current = queue.popleft()
                if current:
                    layer.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
                
            if layer:
                result.append(layer)
        
        return result

