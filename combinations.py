class Solution(object):
    def combine(self, n, k):
        res = []
        def backTrack(start, step, tmp):
            if step == k:
                res.append(tmp)
                return

            for i in range(start, n+1):
                backTrack(i+1, step+1, tmp+[i])
        backTrack(1,0,[])
        return res

n = 4
k = 2
a = Solution()
print(a.combine(n, k))