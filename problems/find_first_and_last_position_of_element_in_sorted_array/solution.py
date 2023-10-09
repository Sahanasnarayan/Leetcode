class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        start = -1
        end = -1

        while low <= high:
            if nums[low] != target:
                low += 1
            elif nums[high] != target:
                high -= 1
            else:
                start = low
                end = high
                break  # Exit the loop once both start and end are found

        return [start, end]