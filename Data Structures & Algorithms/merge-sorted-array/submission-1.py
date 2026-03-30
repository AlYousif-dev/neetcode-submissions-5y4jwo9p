class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0 
        k = m+n
        for i in range(m,m+n):
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
        for i in range(k-1):
            for l in range(k-i-1):
                if nums1[l] > nums1[l+1]:
                    nums1[l], nums1[l+1] = nums1[l+1], nums1[l]
            

