#!/usr/bin/python
# -* - coding: UTF-8 -* -

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        maxArea = 0
        m = len(grid)
        print m
        n = len(grid[0])
        for i in range (m):
            for j in range (n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea,self.findMax(grid,i,j))
        return maxArea
    def findMax(self,grid,i,j):
        if(i >= 0 and i < len(grid) and j >=0 and j < len(grid[0]) and grid[i][j] == 1):
            grid[i][j] = 0
            return 1 + self.findMax(grid,i+1,j) + self.findMax(grid,i-1,j) + self.findMax(grid,i,j+1) + self.findMax(grid,i,j-1)
        else:
            return 0


if __name__ == '__main__':
    # grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    solution = Solution()
    solution.maxAreaOfIsland(grid)

