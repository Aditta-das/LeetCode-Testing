class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while True:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
        return [l, r]

numbers = [1, 3, 4, 5, 7, 10, 11]
target = 21
a = Solution()
print(a.twoSum(numbers, target))