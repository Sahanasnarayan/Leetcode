class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        reshaped_matrix = [[0] * c for _ in range(r)]
        row_idx = 0
        col_idx = 0

        for i in range(rows):
            for j in range(cols):
                reshaped_matrix[row_idx][col_idx] = mat[i][j]
                col_idx += 1
                if col_idx == c:
                    col_idx = 0
                    row_idx += 1

        return reshaped_matrix