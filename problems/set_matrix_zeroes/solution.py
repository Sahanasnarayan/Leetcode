class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_zero = set()
        cols_to_zero = set()

    # Step 1: Find rows and columns with zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

    # Step 2: Set rows to zeros
        for row in rows_to_zero:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

    # Step 3: Set columns to zeros
        for col in cols_to_zero:
            for i in range(len(matrix)):
                matrix[i][col] = 0