class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
         res=[]
         slate=[]
         csum=0
         self.helper(nums,target,slate,csum,0,res)
         return res

    def helper(self,nums:List[int],target:int,slate,csum,index,res):
         if csum==target:
                res.append(slate[:])
                return
         elif csum>target:
                return
         for i in range(index,len(nums)):
                csum+=nums[i]  
                slate.append(nums[i])
                self.helper(nums,target,slate,csum,i,res)  
                slate.pop()
                csum-=nums[i]    