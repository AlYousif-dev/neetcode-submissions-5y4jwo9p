class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def search(root, arr):
            if root is None:
                arr.append("#")  # use marker instead of None for string conversion
                return
            arr.append(str(root.val))
            search(root.left, arr)
            search(root.right, arr)

        arr1, arr2 = [], []
        search(root, arr1)
        search(subRoot, arr2)

        s1 = ",".join(arr1)
        s2 = ",".join(arr2)

        return s2 in s1