class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for inner in grid:
            for ele in inner:
                if ele < 0:
                    result += 1

        return result
        