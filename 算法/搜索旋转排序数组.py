#!/usr/bin/python
# -* - coding: UTF-8 -* -
INF = 0x3f3f3f3f


class Solution(object):

    def valueOf(self, x, nums):
        return x + INF if x < nums[0] else x

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            elif self.valueOf(nums[mid], nums) > self.valueOf(target, nums):
                r = mid - 1
            else:
                print self.valueOf(nums[mid], nums)
                print self.valueOf(target, nums)
                l = mid + 1
        return -1


if __name__ == '__main__':

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    solution = Solution()
    print solution.search(nums, target)

