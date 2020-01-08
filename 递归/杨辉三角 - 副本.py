#!/usr/bin/python
# -* - coding: UTF-8 -* -


# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#
#         result = []
#         for i in range(numRows):
#             temp = [1] * (i + 1)
#             for j in range(i+1):
#                 if i == j or j == 0:
#                     temp[j] = 1
#                 else:
#                     temp[j] = result[i - 1][j - 1] + result[i - 1][j]
#             result.append(temp)
#         return result

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(i+1):
                if j != i and j != 0:
                    row[j] = result[i-1][j] + result[i-1][j-1]

            result.append(row)

        return result



if __name__ == '__main__':

    so = Solution()
    #print so.generate(3)
    s = """skill38.shjt2	4e8e9971108e80af3abefe7105ce8868+aacc57efde66779620131d81e776bcd26f17c1e6	epc	%5Cwindows%5Csyswow64%5Cwindowspowershell%5Cv1.0%5Cmodules%5Cbranchcache%5Cbranchcacheprimarypublicationcachefile.cd
xml	-1	10	1	0	branchcacheprimarypublicationcachefile.cdxml	0	ed571229e70e49af897d2f9179415d13	360ent	0	0	1575474616	10.0.16299.256.1.0.48	4		0  -
0	0	0			ext%3A1%2C%7C%7C%7C%7Cent_id%3A2%2CMjAzMDc4fHxjY2lkOjU5OUM2RkQ1LTU3QjItQTQ4QS05NEQxLUUyNkMxQzhBMzQ5M3x8%7C%7C	407	1045	0		0	116.6.121.130	0	-1 -
-1	10.0	-1.-1		1	2	1	0	-1.-1.-1.-1.-1.-1	|			11.00.16299.371 (WinBuild.160101.0800)	4	HTTP		12.8.0.1007	-1.-1			u2h=
0|noconf=0			utf8	0	CN%7C%E5%B9%BF%E4%B8%9C%7C%E7%8F%A0%E6%B5%B7%7C519000%7C0756%7C%E7%94%B5%E4%BF%A1%7C2%7C1%7C0%7C		7b630c35213f41a85f1759a8f4644c30d051beec2b8b	h_home_haohu
a"""
    a = s.split('\t')
    print a[59]
    print len(a)
    import numpy
    numpy.ara

