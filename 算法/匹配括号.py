#!/usr/bin/python
# -* - coding: UTF-8 -* -


class Solution(object):
    # 用堆栈实现
    def match(self, s):
        """
        :type s: Str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
            if i == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

    # 若字符串内全为括号，改为变量实现
    def match1(self, s):
        sum = 0
        for i in s:
            if i == '(':
                sum += 1
            else:
                if sum > 0:  # 这里是防止前面没有左括号(，出现右括号却减为负数
                    sum -= 1
        if sum:
            return False
        else:
            return True

    # 若字符串内全为括号，找出最长匹配长度，如(()为2
    def match2(self, s):
        # max_len = 0
        # left_count = 0
        # right_count = 0
        # for i in s:
        #     if i == '(':
        #         left_count += 1
        #     else:
        #         right_count += 1
        #     if left_count == right_count:
        #         max_len = max(max_len, 2 * left_count)
        #     if right_count > left_count:
        #         left_count = right_count = 0
        # left_count = 0
        # right_count = 0
        # for i in s[::-1]:  # 从右往左匹配
        #     if i == '(':
        #         left_count += 1
        #     else:
        #         right_count += 1
        #     if left_count == right_count:
        #         max_len = max(max_len, 2 * left_count)
        #     if left_count > right_count:
        #         left_count = right_count = 0
        # return max_len
        max_len = 0
        sum = 0
        left_count = 0
        right_count = 0
        for i in s:
            if i == '(':
                left_count += 1
                sum += 1
            else:
                if sum > 0:
                    sum -= 1
                    right_count += 1
        max(max_len, 2 * left_count)

        left_count = 0
        right_count = 0
        for i in s[::-1]:  # 从右往左匹配
            if i == '(':
                left_count += 1
            else:
                right_count += 1
            if left_count == right_count:
                max_len = max(max_len, 2 * left_count)
            if left_count > right_count:
                left_count = right_count = 0
        return max_len



if __name__ == '__main__':
    # grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    s = '((hello))'
    # FIX_ME 下面为2
    s1 = ')()(()'
    s1= '(()(()'
    solution = Solution()
    print solution.match2(s1)


