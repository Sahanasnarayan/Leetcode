class Solution:
    def count_set_bits(self, num: int) -> int:
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total_sum = 0
        for i in range(len(nums)):
            if self.count_set_bits(i) == k:
                total_sum += nums[i]
        return total_sum