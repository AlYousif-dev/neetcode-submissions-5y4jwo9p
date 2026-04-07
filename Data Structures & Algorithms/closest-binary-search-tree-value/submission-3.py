# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = {}

        def search(root,diff):
            if root is None:
                return diff
            
            diff[abs(root.val-target)] = root.val
            search(root.left,diff)
            search(root.right,diff)
            return diff
        diff = search(root,diff)
        return diff[min(diff)]
        