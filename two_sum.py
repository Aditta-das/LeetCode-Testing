class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, j in enumerate(nums):
            m = target - j
            if m in d:
                return [d[m], i]
            else:
                d[j] = i

a = Solution()
nums = [2, 11, 7, 12]
target = 9

print(a.twoSum(nums, target))