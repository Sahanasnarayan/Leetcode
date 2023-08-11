class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
        # Find the smallest number greater than nums[i] to the right of nums[i]
           j = len(nums) - 1
           while nums[j] <= nums[i]:
               j -= 1
        # Swap nums[i] and nums[j]
           nums[i], nums[j] = nums[j], nums[i]

    # Reverse the order of numbers after index i
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        