class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, j in enumerate(nums):
            m = target - j
            print(f"m val: {m}")
            if m in d:
                print(d[m], i)
                return [d[m], i]
            else:
                d[j] = i

a = Solution()
nums = [2, 11, 7, 12]
target = 9

print(a.twoSum(nums, target))