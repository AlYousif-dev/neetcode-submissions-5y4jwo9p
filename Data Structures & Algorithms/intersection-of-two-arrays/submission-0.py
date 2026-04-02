class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        check = 0
        flag = False
        if len(nums1) < len(nums2):
            check = len(nums1)
        elif len(nums1) > len(nums2):
            check = len(nums2)
            flag = True
        else:
            check = len(nums1)
        arr = []

        for i in range(check):
            if flag and nums2[i] in nums1:
                seen.add(nums2[i])
            elif nums1[i] in nums2:
                seen.add(nums1[i])
        for num in seen:
            arr.append(num)

        return arr