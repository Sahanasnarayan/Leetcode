class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        start = -1
        end = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                start = end = mid
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if start != -1:
            # Search towards the left to find the starting position
            left = start - 1
            while left >= 0 and nums[left] == target:
                start = left
                left -= 1

            # Search towards the right to find the ending position
            right = end + 1
            while right < len(nums) and nums[right] == target:
                end = right
                right += 1

        return [start, end]