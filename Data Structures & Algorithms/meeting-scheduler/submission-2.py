class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        p1 = 0
        p2 = 0
        slots1.sort()
        slots2.sort()
        while p1 < len(slots1) and p2 < len(slots2):
            intersect_start = max(slots1[p1][0], slots2[p2][0])
            intersect_end = min(slots1[p1][1], slots2[p2][1])
            
            if intersect_end - intersect_start >= duration:
                return [intersect_start, intersect_start + duration]
            
            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
                
        return []
