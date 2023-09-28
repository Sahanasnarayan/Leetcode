class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        rp=0
        lp=len(nums)-1
        while(rp<lp):
            if (nums[rp]%2 == 0):
                rp+=1
            if (nums[lp]%2 == 1):
                lp-=1
            elif((nums[rp]%2==1) and (nums[lp]%2==0)):
                nums[rp],nums[lp]=nums[lp],nums[rp]
                rp+=1
                lp-=1     
        return nums          