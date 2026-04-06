# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preOrder(root,arr):
            if root is None:
                return arr.append(None)
            arr.append(root.val)
            preOrder(root.left,arr)
            preOrder(root.right,arr)
            return arr
        arr1 = []
        arr2 = []
        return preOrder(q,arr1) == preOrder(p,arr2)
