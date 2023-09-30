class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        actualsum=0
        numssum=0
        for i in range(1,n+1):
            actualsum+=i
            numssum+=nums[i-1]
        return actualsum-numssum        