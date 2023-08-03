class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums1:
            ind = nums2.index(n)
            flag = False
            for i in range(ind, len(nums2)):
                if nums2[i] > n:
                    result.append(nums2[i])
                    flag = True
                    break
            if not flag:
                result.append(-1)
        return result        