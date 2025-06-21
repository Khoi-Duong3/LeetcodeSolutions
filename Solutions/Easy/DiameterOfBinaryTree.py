class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]

        def height(root):
            if not root:
                return 0
            
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            diameter = leftHeight + rightHeight

            maxDiameter[0] = max(maxDiameter[0], diameter)

            return 1 + max(leftHeight, rightHeight)
        
        height(root)

        return maxDiameter[0]