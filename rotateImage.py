class Solution(object):
    def rotate(self, matrix):
        N = len(matrix)
        matrix.reverse()
        for r in range(N):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
a = Solution()
print(a.rotate(matrix))