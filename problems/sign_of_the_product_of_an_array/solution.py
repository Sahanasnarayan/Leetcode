class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x=1
        for i in range(len(nums)):
            x=x*nums[i]
        if(x>0):
            return 1
        if(x==0):
            return 0
        else:
            return -1           