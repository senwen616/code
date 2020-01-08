#!/usr/bin/python
# -* - coding: UTF-8 -* -

class Solution(object):
    class Solution:
        def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
            y, g = z, customfunction.f
            for x in range(1, z + 1):
                while y:
                    d = g(x, y) - z
                    if d <= 0:
                        if not d:
                            yield [x, y]
                        break
                    y -= 1
                if not y:
                    return


if __name__ == '__main__':
    # grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    solution = Solution()
    print 'asd'
    print solution.maximalSquare(matrix)

