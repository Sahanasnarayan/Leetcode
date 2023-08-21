class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope_x = coordinates[0][0] - coordinates[1][0]
        slope_y = coordinates[0][1] - coordinates[1][1]

        for i in range(2,len(coordinates)):
            if (coordinates[i][0] - coordinates[0][0])*slope_y != (coordinates[i][1] - coordinates[0][1])*slope_x:
                return False
        return True