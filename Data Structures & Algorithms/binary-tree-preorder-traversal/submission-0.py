# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def preOrder(root,arr):
            if root is None:
                return arr
            arr.append(root.val)
            preOrder(root.left,arr)
            preOrder(root.right,arr)
            return arr
        return preOrder(root,arr)