class Solution:
    def twoSum(self, nums, target):
        output = {}
        for i, j in enumerate(nums):
            m = target - j
            if m in output:
                return [output[m], i]
            else:
                output[j] = i

nums = [2,7,11,15]
target = 22
a = Solution()
print(a.twoSum(nums, target))