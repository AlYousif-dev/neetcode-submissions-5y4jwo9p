# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postOrder(root,arr):
            if root is None:
                return arr
            
            postOrder(root.left,arr)
            postOrder(root.right,arr)
            arr.append(root.val)

            return arr
        post_order_arr = []
        return postOrder(root,post_order_arr)