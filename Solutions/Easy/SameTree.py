# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = [True]

        def isSame (root1, root2):
            if same[0] is False:
                return

            if (not root1 and root2) or (root1 and not root2):
                same[0] = False
                return

            if not root1 and not root2:
                return
            
            if root1.val != root2.val:
                same[0] = False
            
            isSame(root1.left, root2.left)
            isSame(root1.right, root2.right)

            return
        
        isSame(p,q)

        return same[0]

            