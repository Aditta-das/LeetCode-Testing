class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            while j <= len(nums) - 3:
                k = j + 1
                r = len(nums) - 1
                while k < r:
                    temp = nums[i] + nums[j] + nums[k] + nums[r]
                    if temp == target:
                        res.append([nums[i], nums[j], nums[k], nums[r]])
                        while nums[k] == nums[k+1]:
                            k+=1
                        while nums[r] == nums[r-1]:
                            r-=1
                        k+=1
                        r-=1
                    elif temp < target:
                        k+=1
                    else:
                        r-=1
                j+=1
        return res

nums = [1,0,-1,0,-2,2]
target = 0
a = Solution()
print(a.fourSum(nums, target))