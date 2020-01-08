#!/usr/bin/python
# -* - coding: UTF-8 -* -

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        max_len = 0
        for i in range(1,m):
            for j in range(1, n):
                if int(matrix[i][j]) == 1:
                    matrix[i][j] = min(int(matrix[i][j-1]),int(matrix[i-1][j]),int(matrix[i-1][j-1])) + 1
                    print matrix[i][j]
                    max_len = max(matrix[i][j], max_len)
                else:
                    matrix[i][j] = 0
        return max_len**2


if __name__ == '__main__':
    # grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    solution = Solution()
    print 'asd'
    print solution.maximalSquare(matrix)

