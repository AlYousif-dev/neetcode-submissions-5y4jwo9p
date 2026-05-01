class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2 = {}
        res = [0 for _ in range(len(nums1))]
        for i in range(len(nums2)):
            n2[nums2[i]] = i
        for j in range(len((nums1))):
            res[j] = n2[nums1[j]]
        return res