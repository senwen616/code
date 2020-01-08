#!/usr/bin/python
# -* - coding: UTF-8 -* -

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """



if __name__ == '__main__':
    # grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    solution = Solution()
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    envelopes.sort(key=lambda a: (a[0], -a[1]))
    print envelopes
    n1 = []
    nums = []
    for i in range(len(envelopes)):
        n1.append(envelopes[i][0])
        nums.append(envelopes[i][1])
    mem = []
    for i in range(len(nums)):
        low, upper = 0, len(mem)
        while low < upper:
            mid = (upper - low) // 2 + low
            if mem[mid] < nums[i]:

                low = mid + 1
            else:
                upper = mid

        if upper == len(mem):
            if n1[i] != n1[i - 1]:
                mem.append(nums[i])
        else:
            mem[upper] = nums[i]
print  mem