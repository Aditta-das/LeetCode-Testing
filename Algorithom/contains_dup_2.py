class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            elif abs(i - dict[nums[i]]) <= k:
                return True
            else:
                dict[nums[i]] = i
        return False

nums = [1,0,1,1]
k = 1
a = Solution()
print(a.containsNearbyDuplicate(nums, k))