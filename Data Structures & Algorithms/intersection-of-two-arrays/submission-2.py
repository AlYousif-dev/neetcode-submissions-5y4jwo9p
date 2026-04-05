class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()

        arr = []
        for i in range(len(nums1)):
            if nums1[i] not in seen:
                seen.add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] in seen and nums2[i] not in arr:
                arr.append(nums2[i])
        return arr