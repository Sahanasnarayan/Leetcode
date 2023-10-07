class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = {}
        count = 0
        i = 0

        while i < len(nums):
            num = nums[i]
            if num not in ans:
                ans[num] = 1
                count += 1
            elif ans[num] < 2:
                ans[num] = 2
                count += 1
            else:
                nums.pop(i) 
                continue 
            i += 1
        return count