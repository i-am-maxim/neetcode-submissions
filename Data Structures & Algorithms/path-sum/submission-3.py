# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def preorder(root, target):
            if not root:
                return False
            if root.left is None and root.right is None:
                return target - root.val == 0
            left = preorder(root.left, target-root.val)
            right = preorder(root.right, target-root.val)
            return left or right
            
        return preorder(root, targetSum)
                
        
        