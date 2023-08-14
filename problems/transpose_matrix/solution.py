class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []
        for i in range(len(matrix[0])):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[j][i])
            transposed.append(tmp)
        return transposed
        # this is also the better approach, u have to use two appends since u need it in the form of matrix