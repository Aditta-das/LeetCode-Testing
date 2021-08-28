class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []

        def backTrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return 

            if openN < n:
                stack.append('(')
                backTrack(openN + 1, closeN)
                stack.pop()

            if openN > closeN:
                stack.append(")")
                backTrack(openN, closeN + 1)
                stack.pop()

        backTrack(0, 0)
        return res


a = Solution()
print(a.generateParenthesis(3))