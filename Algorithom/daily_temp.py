class Solution:
    def dailyTemperatures(self, temp):
        '''
        temp[i] less then temp[i+1] : append
        '''
        stack = []
        res = [0] * len(temp)
        for i, t in enumerate(temp):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res


temperatures = [73,74,75,71,69,72,76,73]
a = Solution()
print(a.dailyTemperatures(temperatures))