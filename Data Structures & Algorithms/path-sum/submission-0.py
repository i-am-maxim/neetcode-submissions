# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def postorder(root, target):
            if not root:
                return False
            if root.left is None and root.right is None:
                return target - root.val == 0
            left = postorder(root.left, target-root.val)
            right = postorder(root.right, target-root.val)
            return left or right
            
        return postorder(root, targetSum)
                
        
        