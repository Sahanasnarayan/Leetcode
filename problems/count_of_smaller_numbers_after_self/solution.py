class Solution(object):
    def countSmaller(self, nums):
        counts = [0] * len(nums)
        sorted_nums = []

        for i in range(len(nums)-1, -1, -1):
            index = self.binary_search(sorted_nums, nums[i])
            counts[i] = index
            sorted_nums.insert(index, nums[i])

        return counts

    def binary_search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left