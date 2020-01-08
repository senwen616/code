#!/usr/bin/python
# -* - coding: UTF-8 -* -

class Solution0(object): # 一行
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) - 1, 0, -1): s.insert(i, s.pop(0))

class Solution1(object): # 递归
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s
        else:
            return self.reverseString(s[1:]) + [s[0]]


class Solution2(object): # 双指针
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1; j -= 1


if __name__ == '__main__':
    s = ['h','e','l','l','o']
    so = Solution2()
    so.reverseString(s)
    print s
