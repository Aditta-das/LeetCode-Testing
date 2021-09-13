class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        def backTrack(start, step, tmp, curr_sum):
            if step == k and curr_sum == n:
                res.append(tmp[:])
            elif step >= k or curr_sum > n:
                return
            else:
                for i in range(start, 10):
                    backTrack(i+1, step+1, tmp+[i], curr_sum+i)
        backTrack(1, 0, [], 0)
        return res

k = 3
n = 7
a = Solution()
print(a.combinationSum3(k, n))
