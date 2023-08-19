
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_set = set(nums2)
        common = None  
        
        for num in nums1:
            if num in nums2_set:
                if common is None or num < common:
                    common = num
        
        return common if common is not None else -1    
