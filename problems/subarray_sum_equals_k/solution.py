class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #use prefix sum
        count, sums = 0, 0
        hashmap = {}
        hashmap[0] = 1
        for i in range(len(nums)):
            sums += nums[i]
            if sums-k in hashmap:
                count += hashmap[sums-k]
            if sums not in hashmap:
                hashmap[sums] = 1
            else:
                hashmap[sums] += 1
        return count
        
        
        
        
