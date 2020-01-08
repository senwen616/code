#!/usr/bin/python
# -* - coding: UTF-8 -* -


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def Max_tree(self, nums):
        try:

            temp = nums[:]
            temp.sort()
            Max = temp[-1]
            node = TreeNode(Max)
            index = nums.index(Max)
            node.left = self.Max_tree(nums[:index])
            node.right = self.Max_tree(nums[index + 1:])
            return node
        except:
            pass

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.Max_tree(nums)


if __name__ == '__main__':
    # grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    nums = [3,2,1,6,0,5]
    solution = Solution()
    print solution.constructMaximumBinaryTree(nums)
