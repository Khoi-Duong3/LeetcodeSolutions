from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range (len(matrix)):
            for j in range (i+1, len(matrix[0])):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp

        for i in range (len(matrix)):
            for j in range (len(matrix)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][(len(matrix) - j - 1)]
                matrix[i][(len(matrix) -j - 1)] = temp