class Solution(object):
    def trap(self, height):
        size = len(height)
        left = size * [0]
        right = size * [0]
        left[0] = height[0]
        max_left = height[0]
        total_unit_water = 0

        for idx in range(0, size):
            if (max_left < height[idx]):
                max_left = height[idx]
                left[idx] = max_left
            else:
                left[idx] = max_left

        max_right = height[-1]
        for idx in range(size-1, -1, -1):
            if (max_right < height[idx]):
                max_right = height[idx]
                right[idx] = max_right
            else:
                right[idx] = max_right
        
        for i in range(0, size):
            total_unit_water = total_unit_water + min(left[i], right[i]) - height[i]
        return total_unit_water

    # second way
    def trap2(self, height):
        waterLevel = []
        left = 0
        for h in height:
            left = max(left, h)
            waterLevel += [left]
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterLevel[i] = min(waterLevel[i], right) - h  
        return sum(waterLevel)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
a = Solution()
print(a.trap(height))