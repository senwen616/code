#!/usr/bin/python
# -* - coding: UTF-8 -* -


class Solution(object):
    def frog_jump(self, num):
        """
        :type num: int
        :rtype: List[List[int]]
        """
        # a, b = 1, 2
        # for i in range(num-3):
        #    a, b = b, a+b
        # return a+b
        if num < 3:
            return num
        else:
            return self.frog_jump(num-1) + self.frog_jump(num-2)
if __name__ == '__main__':

    so = Solution()
    print so.frog_jump(5)

