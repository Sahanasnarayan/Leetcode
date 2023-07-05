class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to handle duplicates
        subsets = []
        self.backtrack(nums, 0, [], subsets)
        return subsets

    def backtrack(self, nums: List[int], start: int, curr_subset: List[int], subsets: List[List[int]]):
        # Add the current subset to the list of subsets
        subsets.append(curr_subset[:])

        for i in range(start, len(nums)):
            # Skip duplicates to avoid duplicate subsets
            if i > start and nums[i] == nums[i - 1]:
                continue

            # Choose the current element
            curr_subset.append(nums[i])

            # Explore next elements
            self.backtrack(nums, i + 1, curr_subset, subsets)

            # Backtrack by removing the current element
            curr_subset.pop()
        