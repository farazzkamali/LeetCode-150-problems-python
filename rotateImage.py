class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Reverse the matrix
        matrix.reverse()

        # Transpose the matrix in place
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# class Solution:
#     def rotate(self, matrix):
#         matrix.reverse()
#         matrix = list(zip(*matrix[:]))
#         matrix = [list(row) for row in matrix]
