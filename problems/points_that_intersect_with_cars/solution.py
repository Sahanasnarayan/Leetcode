class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
  
        covered_points = set()

    # Iterate through the parking spots
        for start, end in nums:
            for point in range(start, end + 1):
                if point not in covered_points:
                    covered_points.add(point)

    # Return the count of unique covered points
        return len(covered_points)



