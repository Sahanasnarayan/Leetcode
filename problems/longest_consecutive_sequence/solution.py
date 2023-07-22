class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longeststreak=0
        for num in numset:
            if num - 1 not in numset:
                curr=num
                currstreak=1
                while curr+1 in numset:
                    curr+=1
                    currstreak+=1
                longeststreak= max(longeststreak,currstreak)
        return longeststreak            