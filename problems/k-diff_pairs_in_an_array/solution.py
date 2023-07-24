class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        left=0
        right=1
        count=0
        seen=set()
        while(right<len(nums)):
            if nums[right]-nums[left] == k:
                if nums[left] not in seen:

                    count+=1
                    seen.add(nums[left])
                    
                left+=1
                right=left+1
            elif nums[right]-nums[left] > k:
                left+=1
                right=left+1
            else: 
                right+=1    
        return count #use se and rectify by urself
