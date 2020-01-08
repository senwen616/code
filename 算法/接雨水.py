#!/usr/bin/python
# -* - coding: UTF-8 -* -


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        total = 0
        left = 0
        right = max(height)

        for i in range(len(height)):
            try:
                if i>0:
                    left = max(left, height[i - 1])
                if height[i] == right:
                    right = max(height[i + 1:])
            except:
                pass
            if height[i] < min(left, right):
                total += min(left, right) - height[i]
                print total, i
        return total


if __name__ == '__main__':
    # grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()
    print solution.trap(height)

