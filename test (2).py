#! usr/bin/env python
# -*-coding: utf-8-*-

import re


# print re.findall(r'\%\>','% >sd')
# nums = [-1, 3, 4, -5, 7, -5]
"""
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)

    def bubble_sort(self, nums):
        for i in range(len(nums) - 1):
            ex_flag = False  # 改进后的冒泡，设置一个交换标志位
            for j in range(len(nums) - i - 1):

                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    ex_flag = True
                if not ex_flag:
                    return nums  # 这里代表计算机偷懒成功 (〃'▽'〃)

        return nums

"""


class Solution(object):
    def findMax(self, num):
        l = 0
        bi = list(bin(num).replace('0b', '').rjust(8,'0'))
        for i in range(len(bi)):
            if int(bi[i]) == 1:
                l += 1
            else:
                return l

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        l = self.findMax(data[0])
        if l == 0:
            self.validUtf8(data[1:-1])
        elif l == 1:
            return False
        elif l == 2:
            if self.findMax(data[1]) == 1:
                self.validUtf8(data[2:-1])
            else:
                return False
        elif l == 3:
            if self.findMax(data[1]) == 1 and self.findMax(data[2]) == 1:
                self.validUtf8(data[3:-1])
            else:
                return False
        elif l == 4:
            if self.findMax(data[1]) == 1 and self.findMax(data[2]) == 1 and self.findMax(data[3]) == 1:
                self.validUtf8(data[4:-1])
            else:
                return False
        return True
if __name__ == "__main__":
    a = [1,2]
    b = ['shuliang', 'zhiliang']
    print dict(zip(a, b))
    '''
    cl = Solution()
    nums = [235,140,4]
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    #print cl.maxSubArray(nums)
    #print cl.bubble_sort(nums)
    envelopes.sort(key=lambda a: (a[0], -a[1]))
    #print envelopes
    print cl.validUtf8(nums)
    print 1<<7
    print re.findall(r"http|docs|head|ad","https://adaddocs.httppython.org/3/whatsnew/3.6.html")
    '''