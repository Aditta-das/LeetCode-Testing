class Solution:
    def threeSumClosest(self, nums, target):
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                sums = nums[i] + nums[lo] + nums[hi]
                # print(sums)
                if abs(target - sums) < abs(diff):
                    diff = target - sums
                    # print(diff)
                if sums < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff

nums = [-1,2,1,-4]
target = 1
a = Solution()
print(a.threeSumClosest(nums, target))