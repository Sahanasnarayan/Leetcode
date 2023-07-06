class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        slate=[]
        csum=0
        self.helper(nums,target,slate,csum,0,res)
        return res

    def helper(self,nums:List[int],target: int,slate,csum,index,res):
        if csum==target:
            res.append(slate[:])
            return
        elif csum>target:
            return
        for i in range(index,len(nums)):
            
            if i!=index and nums[i] == nums[i-1]:
                continue
            csum += nums[i]
            slate.append(nums[i])    
            self.helper(nums,target,slate,csum,i+1,res)
            slate.pop()
            csum -= nums[i]               