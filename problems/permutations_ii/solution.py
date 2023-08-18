class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.permuteRecursive(nums, 0, result)
        return result
    
    def permuteRecursive(self, nums, begin, result):
        if begin >= len(nums):
            result.append(nums.copy())
            return
        
        used = set()  # Keep track of used elements at this level
        for i in range(begin, len(nums)):
            if nums[i] in used:
                continue
            used.add(nums[i])
            
            nums[begin], nums[i] = nums[i], nums[begin]
            self.permuteRecursive(nums[:], begin + 1, result)
            nums[begin], nums[i] = nums[i], nums[begin]
            #check out this method . this is best