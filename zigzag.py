class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        space = [''] * numRows
        idx, step = 0, 1

        if numRows >= len(s) and numRows == 1:
            return s

        for w in s:
            space[idx] += w
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step 
        return ''.join(space)  

s = "AB"
numRows = 1

a = Solution()
print(a.convert(s, numRows))