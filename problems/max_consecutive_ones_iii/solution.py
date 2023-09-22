class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == 0:
                k -= 1  # Flip the zero and decrement k
            if k < 0:
                # Flip back the ones to zeros
                if nums[j] == 0:
                    k += 1
                j += 1
            i += 1
        return i - j        
 